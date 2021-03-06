#!/usr/bin/env python
"""This is a Py GTK Glade based video editor. Author - Anshuman Rai 22 Feb 2012"""

import sys 
from opencv.cv import *
from opencv.highgui import *
from opencv import adaptors
import gobject
import cv

import numpy

from pyffmpeg import *

import alsaaudio

import time
import redis_wrap
import redis
import os
from PIL import Image
import math


TS_VIDEO_RGB24={ 'video1':(0, -1, {'pixel_format':PixelFormats.RGB24}), 'audio1':(1,-1,{})}


try:
	import pygtk
	pygtk.require("2.0")
except:
	pass

try:
	import gtk
	import gtk.glade
     	import time

except:
	sys.exit(1)


class AlsaSoundLazyPlayer:
    def __init__(self,rate=44100,channels=2,fps=25):
        self._rate=rate
        self._channels=channels
        self._d = alsaaudio.PCM()
        self._d.setchannels(channels)
        self._d.setformat(alsaaudio.PCM_FORMAT_S16_LE)
        self._d.setperiodsize((rate*channels)//int(fps))
        self._d.setrate(rate)
	self._mute = False
	return
    def push_nowait(self,stamped_buffer):
	if not self._mute:
        	self._d.write(stamped_buffer[0].data)
	return


class VideoEditor:

	def __init__(self):
		
		self.gladeFile = "videoeditor.xml"
        	self.builder = gtk.Builder()
        	self.builder.add_from_file(self.gladeFile)


		self.adDictionaryFileBeginFrame = redis_wrap.get_hash('adDictionaryFileBeginFrame')
		self.adDictionaryFileEndFrame = redis_wrap.get_hash('adDictionaryFileEndFrame')
		self.window = self.builder.get_object("MainWindow")
		self.window.resize(840,640)
		self.hboxPlayBack = self.builder.get_object("hboxPlayBack")
		self.hboxEditArrow = self.builder.get_object("hboxEditArrow")
		self.hboxCompose = self.builder.get_object("hboxCompose")
		self.mainNotebookComposeVBox = self.builder.get_object("MainNotebookComposeVBox")
		self.mainNotebookComposeVBoxImage = self.builder.get_object("MainNotebookComposeVBoxImage")
		self.buttonComposePaneVBoxAdd = self.builder.get_object("buttonComposePaneVBoxAdd")
		self.mainNotebookImagePlayback = self.builder.get_object("MainNotebookImagePlayback")
		self.hboxPlayBack.show()
		self.hboxEditArrow.hide()
		self.hboxCompose.hide()
		self.hboxEdit = self.builder.get_object("hboxEdit")
		self.mainFrameImage = self.builder.get_object("MainFrameImage")
		self.mainNotebookImagePlayback = self.builder.get_object("MainNotebookImagePlayback")
		self.mainNotebookEditScrolledWindow = self.builder.get_object("MainNotebookEditScrolledWindow")
		self.scale = self.builder.get_object("scale")
		self.timeLabel = self.builder.get_object("timeLabel")
		self.currFilePlaybackFrameNum = 0
		self.currFilePlaybackCurrTimeInSeconds = 0
		self.currFilePlaybackTotalTimeInSeconds = 0
		self.frameRGB = None
    		self.snd=None
		self.playbackMode = False
		self.playbackPaused = False
		self.playbackMpegReader = None
		self.playbackMpegReaderTracks = None
		self.playbackTimer = None
		self.playbackTimeInSecondsFromScale = 0
		self.trimAdsPlaybackMode = False
		self.adLoadMpegReader = None
		self.adLoadMpegReaderTracks = None
		self.trimAdsPlaybackMpegReader = None
		self.trimAdsPlaybackMpegReaderTracks = None
		self.trimAdsPlaybackTimer = None
		self.skipAdFrames = False
		self.currAdFramesToSkip = 0
		self.saveTrimAdsMpegReader = None
		self.imageHashCounter = 0
		self.imagePlaybackCounter = 0
	 	self.trimAdsDisplayBeginReInit = False
		if (self.window):
			dic = { "on_MainWindow_destroy" : gtk.main_quit,
				"on_MainMenuBar_file_open_activate" : self.main_menu_bar_file_open_activate,
				"on_MainMenuBar_ad_load_activate" : self.main_menu_bar_ad_load_activate,
				"on_MainMenuBar_clear_ad_database_activate" : self.main_menu_bar_clear_ad_database_activate,
				"on_buttonPlay_clicked" : self.on_button_play_clicked,
				"on_buttonStop_clicked" : self.on_button_stop_clicked,
				"on_buttonKMeans_clicked" : self.on_button_kmeans_clicked,
				"on_buttonTrimAds_clicked" : self.on_button_trim_ads_clicked,
				"on_buttonSaveTrimAds_clicked" : self.on_button_save_trim_ads_clicked,
				"on_button_compose_pane_vbox_add_clicked" : self.on_button_compose_pane_vbox_add_clicked,
				"on_button_add_clicked" : self.on_button_add_clicked,
				"on_button_export_clicked" : self.on_button_export_clicked,
				"on_MainNotebook_switch_page" : self.on_MainNotebook_switch_page,
				"on_scale_change_value" : self.on_scale_change_value,
				"on_button_pause_clicked" : self.on_button_pause_clicked,
				"on_button_in_clicked" : self.on_button_in_clicked,
				"on_button_out_clicked" : self.on_button_out_clicked,
				"on_scale_motion_notify_event" : self.on_scale_motion_notify_event
				}
			self.builder.connect_signals(dic)
			self.window.show()
		return
	

    	def displayframe(self,thearray):
      		"""
      		pyffmpeg callback
      		"""
		self.imagePlaybackCounter = self.imagePlaybackCounter + 1
		im = Image.fromarray(thearray)
		im.save('frameplay' + str(self.imagePlaybackCounter) + '.jpg', 'jpeg')	

		pixBuf = gtk.gdk.pixbuf_new_from_array(thearray, gtk.gdk.COLORSPACE_RGB, 8) 
		self.mainNotebookImagePlayback.set_from_pixbuf(pixBuf)
                self.mainNotebookImagePlayback.queue_draw()
		self.currFilePlaybackFrameNum = self.currFilePlaybackFrameNum + 1
		self.currFilePlaybackNewTimeInSeconds = int(self.currFilePlaybackFrameNum/self.currFilePlaybackFps)
		if not (self.currFilePlaybackNewTimeInSeconds == self.currFilePlaybackCurrTimeInSeconds):
			self.currFilePlaybackNewTimeInHHMMSS = time.strftime('%H:%M:%S', time.gmtime(self.currFilePlaybackNewTimeInSeconds))
			self.scale.set_value(self.currFilePlaybackNewTimeInSeconds)
			self.timeLabel.set_text(self.currFilePlaybackNewTimeInHHMMSS)
			self.currFilePlaybackCurrTimeInSeconds = self.currFilePlaybackNewTimeInSeconds
		return

		
	def one_pass_algo(self, filename):
		system_cmd_string = './algo ' + filename + ' 2>/dev/null'
		os.system(system_cmd_string)
		algo_output_file = open('algo.out')
		retval = int(algo_output_file.read(4))
		algo_output_file.close()
		return retval

	def main_menu_bar_file_open_activate(self, widget):
		self.fileChooserDialog = gtk.FileChooserDialog(title=None,action=gtk.FILE_CHOOSER_ACTION_OPEN,
                                  buttons=(gtk.STOCK_CANCEL,gtk.RESPONSE_CANCEL,gtk.STOCK_OPEN,gtk.RESPONSE_OK))
		self.fileChooserDialogResponse=self.fileChooserDialog.run()
		if self.fileChooserDialogResponse == gtk.RESPONSE_OK:	
			self.currentFileSelectedFullPathName = self.fileChooserDialog.get_filename()
		self.fileChooserDialog.destroy()
		return	

	def main_menu_bar_ad_load_activate(self, widget):
		self.fileChooserDialog = gtk.FileChooserDialog(title=None,action=gtk.FILE_CHOOSER_ACTION_OPEN,
                                  buttons=(gtk.STOCK_CANCEL,gtk.RESPONSE_CANCEL,gtk.STOCK_OPEN,gtk.RESPONSE_OK))
		self.fileChooserDialogResponse = self.fileChooserDialog.run()
		if self.fileChooserDialogResponse== gtk.RESPONSE_OK : 
			self.currentAdSelectedFullPathName = self.fileChooserDialog.get_filename()
			self.processAdLoad()
		self.fileChooserDialog.destroy()
		return	

	def main_menu_bar_clear_ad_database_activate(self, widget):
		self.clearAdDatabaseDialog = gtk.Dialog(title="Are you sure you want to clear the ad database",parent=None,
                                  buttons=(gtk.STOCK_CANCEL,gtk.RESPONSE_CANCEL,gtk.STOCK_OK,gtk.RESPONSE_OK))
		self.clearAdDatabaseDialog.resize(600,10)
		self.clearAdDatabaseDialogResponse = self.clearAdDatabaseDialog.run()
		if self.clearAdDatabaseDialogResponse== gtk.RESPONSE_OK : 
			#clear the ad dictionaries
			redis_server = redis.Redis('localhost')
			redis_server.delete('adDictionaryFileBeginFrame')
			redis_server.delete('adDictionaryFileEndFrame')
			self.adDictionaryFileBeginFrame = {}
			self.adDictionaryFileEndFrame = {}
		self.clearAdDatabaseDialog.destroy()
		return	

	
	

	def processAdLoad(self):
                ## create the reader object
                self.adLoadMpegReader=FFMpegReader()

                ## open an audio video file
                self.adLoadMpegReader.open(self.currentAdSelectedFullPathName, TS_VIDEO_RGB24)
                self.adLoadMpegReaderTracks=self.adLoadMpegReader.get_tracks()

               	self.adLoadMpegReaderTracks[0].set_observer(self.compute_ad_frame_hash)
		videoCaptureFile = cvCreateFileCapture(self.currentAdSelectedFullPathName);
		self.currAdFps =  int(cvGetCaptureProperty( videoCaptureFile, CV_CAP_PROP_FPS))
		self.currAdNFrames =  int(cvGetCaptureProperty( videoCaptureFile, CV_CAP_PROP_FRAME_COUNT ))
		self.beginAdFramesStored = 0
		cvReleaseCapture(videoCaptureFile)
		print "ad loaded at fps ", self.currAdFps
		print "ad frames", self.currAdNFrames
		#Load the first frame of the ad and store
		self.currAdFrameNumber = 1
                self.adLoadMpegReader.step()


                ## open an audio video file
		#seek till end of the file and seek back
		self.endAdFramesStored = 0
		self.adLoadMpegReaderTracks[0].seek_to_frame(self.currAdNFrames - 3)
                self.adLoadMpegReaderTracks[0].set_observer(self.compute_ad_frame_hash_for_last_frames)
		self.currAdFrameNumber = 1
		try:
                	self.adLoadMpegReader.step()
		except IOError, e:
			print "got io error ", e
			del self.adLoadMpegReader
			return
		del self.adLoadMpegReader
		return

	
	def scale_image(self, im, size):
		im = im.resize((size, size), Image.ANTIALIAS)
		return im

	def gray_scale(self,im):
		im = im.convert('L')
		return im

	def print_pixels(self,im):
		pixels = im.load()
		width, height = im.size
		for x in range(width):
			for y in range(height):
				print pixels[x,y]

	def getBlue(self,im):
		pixels = im.load()
		width, height = im.size
		for x in range(width):
			for y in range(height):
				pixel =  pixels[x,y]
				blue = pixel & 0xff
				im.putpixel((x,y), blue)
		return im

	def initCoefficients(self,size):
		c = numpy.empty((size))
		for i in range(size):
			c[i] = 1
		c[0] = 1/math.sqrt(2)
		return c


	def apply_dct(self,f, size, c):
		pixels = f.load()
		N = size;

		F = numpy.zeros(shape=(N, N))
		for u in range(0,N):
		  	for v in range(0,N):
		    		sum = 0.0;
		    		for i in range(0,N):
		      			for  j in range(0,N):
		        			sum = sum + math.cos(((2*i+1)/(2.0*N))*u*math.pi)*math.cos(((2*j+1)/(2.0*N))*v*math.pi)*(pixels[i,j])
		    		sum = sum * ((c[u]*c[v])/4.0)
		    		F[u,v] = sum
		return F


	def compute_hash_from_dct_vals(self,dctVals, size, smallerSize):
		total = 0.0
		for x in range (0, smallerSize):
			for y in range(0, smallerSize):
		                        total += dctVals[x,y]
		        total -= dctVals[0,0]

		        avg = total / ((smallerSize * smallerSize) - 1)

		       	hash = ""

		        for x in range(0, smallerSize):
		                for y in range(0, smallerSize):
		                        if ((not (x == 0)) and (not (y == 0))): 
						if dctVals[x,y] > avg:
							hash = hash + "1"
						else:
							hash = hash + "0"
			return hash

	def to_decimal(self,x):
	    return sum(map(lambda z: int(x[z]) and 2**(len(x) - z - 1),
		           range(len(x)-1, -1, -1)))


	def compute_dct_hash(self, im):
		im = self.scale_image(im, 32)
		im = self.gray_scale(im)
		im = self.getBlue(im)
		c = self.initCoefficients(32)
		dctVals = self.apply_dct(im, 32, c)
		hash = self.compute_hash_from_dct_vals(dctVals, 32, 8)
		hash = self.to_decimal(hash)
		return hash
	
	



	def computeHash(self,frame):
		im = Image.fromarray(frame)
		im.save("hashimage.jpg", "jpeg")
		hash = self.compute_dct_hash(im)
		return hash
		#im = adaptors.NumPy2PIL(frame)
		#system_cmd_string = "java makeDCTHash hashimage.jpg"
		
		#hashOut = os.popen(system_cmd_string)
		#hashIn = hashOut.readline()
		
		#print "hashIn ", hashIn
		
		#retVal = int(hashIn)
		
		#hashOut.close()
		
		#return retVal
    		#im = im.resize((8, 8), Image.ANTIALIAS).convert('L')
    		#avg = reduce(lambda x, y: x + y, im.getdata()) / 64.
    		#return reduce(lambda x, (y, z): x | (z << y), enumerate(map(lambda i: 0 if i < avg else 1, im.getdata())), 0)

	def hamming(self, h1, h2):
     		h, d = 0, h1 ^ h2
     		while d:
         		h += 1
         		d &= d - 1
     		return h

	def compute_ad_frame_hash(self, thearray):
		computedHash = self.computeHash(thearray)
		print "writing begin frames hash to dictionary ", computedHash
		self.imageHashCounter = self.imageHashCounter + 1
		im = Image.fromarray(thearray)
		im.save('adframe' + str(self.imageHashCounter), 'jpeg')	
		if not (computedHash in self.adDictionaryFileBeginFrame):
			self.adDictionaryFileBeginFrame[computedHash] = self.currentAdSelectedFullPathName
		return
		
	def compute_ad_frame_hash_for_last_frames(self, thearray):
		computedHash = self.computeHash(thearray)
		print "writing last frames hash to dictionary ", computedHash
		self.imageHashCounter = self.imageHashCounter + 1
		im = Image.fromarray(thearray)
		im.save('firstframe' + str(self.imageHashCounter), 'jpeg')	
		if not (computedHash in self.adDictionaryFileEndFrame):
			print "last frames written to dictionary ", computedHash, self.currAdFrameNumber
			self.adDictionaryFileEndFrame[computedHash] = self.currentAdSelectedFullPathName
		return

	def on_button_play_clicked(self, widget):
		self.playbackMode = True
		if not (self.playbackPaused):
			videoCaptureFile = cvCreateFileCapture(self.currentFileSelectedFullPathName);
			self.currFilePlaybackFps =  int(cvGetCaptureProperty( videoCaptureFile, CV_CAP_PROP_FPS))
			self.currFilePlaybackNFrames =  int(cvGetCaptureProperty( videoCaptureFile, CV_CAP_PROP_FRAME_COUNT ))
			self.currFilePlaybackTotalTimeInSeconds = int(self.currFilePlaybackNFrames/self.currFilePlaybackFps);
			self.currFilePlaybackCurrTimeInSeconds = 0
			self.scale.set_range(0, self.currFilePlaybackTotalTimeInSeconds);
			self.currFilePlaybackFrameNum= 0
			self.playbackTimer = gobject.timeout_add(int(1000/self.currFilePlaybackFps), self.playback_handler)
			cvReleaseCapture(videoCaptureFile)
		else:
			self.playbackTimer = gobject.timeout_add(int(1000/self.currFilePlaybackFps), self.playback_handler)
			self.playbackPaused = False
			


	def playback_handler(self):
		if (self.playbackMpegReader == None):
			## create the reader object
			self.playbackMpegReader=FFMpegReader()

			## open an audio video file
			self.playbackMpegReader.open(self.currentFileSelectedFullPathName, TS_VIDEO_RGB24)
			self.playbackMpegReaderTracks=self.playbackMpegReader.get_tracks()

			## connect audio to its device
			self.playbackAP=AlsaSoundLazyPlayer(self.playbackMpegReaderTracks[1].get_samplerate(),self.playbackMpegReaderTracks[1].get_channels(),int(self.playbackMpegReaderTracks[0].get_fps()))
			self.playbackMpegReaderTracks[1].set_observer(self.playbackAP.push_nowait)
			self.playbackMpegReaderTracks[0].set_observer(self.displayframe)
		try:	
			if not (self.playbackTimeInSecondsFromScale == 0):
				if not (self.playbackTimeInSecondsFromScale == self.currFilePlaybackCurrTimeInSeconds ):
					self.currFilePlaybackFrameNum = self.playbackTimeInSecondsFromScale * self.currFilePlaybackFps
					self.playbackMpegReaderTracks[0].seek_to_seconds(self.playbackTimeInSecondsFromScale)
					self.playbackMpegReaderTracks[1].seek_to_seconds(self.playbackTimeInSecondsFromScale)
					self.playbackTimeInSecondsFromScale = 0
			else:
				self.playbackMpegReader.step()
			return 1
		except IOError:
			del self.playbackMpegReader
			self.playbackMpegReader = None
			# Initialize playback scale to 0
			self.scale.set_value(0)
			self.timeLabel.set_text("00:00:00")
			self.playbackMode = False
			return 0
			

	def on_button_trim_ads_clicked(self, widget):
		self.trimAdsPlaybackMode = True
		videoCaptureFile = cvCreateFileCapture(self.currentFileSelectedFullPathName);
		fps =  int(cvGetCaptureProperty( videoCaptureFile, CV_CAP_PROP_FPS))
		cvReleaseCapture(videoCaptureFile)
		self.trimAdsPlaybackTimer = gobject.timeout_add(int(1000/fps), self.trim_ads_playback_handler)
		return

	def trim_ads_playback_handler(self):
		if (self.trimAdsPlaybackMpegReader == None):
			## create the reader object
			self.trimAdsPlaybackMpegReader=FFMpegReader()

			## open an audio video file
			self.trimAdsPlaybackMpegReader.open(self.currentFileSelectedFullPathName, TS_VIDEO_RGB24)
			self.trimAdsPlaybackMpegReaderTracks=self.trimAdsPlaybackMpegReader.get_tracks()

			## connect audio to its device
			self.trimAdsAP=AlsaSoundLazyPlayer(self.trimAdsPlaybackMpegReaderTracks[1].get_samplerate(),self.trimAdsPlaybackMpegReaderTracks[1].get_channels(),int(self.trimAdsPlaybackMpegReaderTracks[0].get_fps()))
			self.trimAdsPlaybackMpegReaderTracks[1].set_observer(self.trimAdsAP.push_nowait)
			self.trimAdsPlaybackMpegReaderTracks[0].set_observer(self.display_ads_trimmed_frame_till_begin)
			return 1
		try:
			self.trimAdsPlaybackMpegReader.step()
			return 1
		except IOError:
			del self.trimAdsPlaybackMpegReader
			self.trimAdsPlaybackMpegReader = None
			self.trimAdsPlaybackMode = False
			return 0


    	def display_ads_trimmed_frame_till_begin(self,thearray):

		if self.trimAdsDisplayBeginReInit:
			im = Image.fromarray(thearray)
			im.save('new.jpg')
      		"""
      		pyffmpeg callback
      		"""
		#if not self.skipAdFrames:
		computedHash = self.computeHash(thearray)

		if computedHash in self.adDictionaryFileBeginFrame:
			print "Found matching ad begin", self.adDictionaryFileBeginFrame[computedHash]
			im = Image.fromarray(thearray)
			im.save("begin.jpg", "jpeg")
				

			self.currAdMatchName =  self.adDictionaryFileBeginFrame[computedHash]
			self.trimAdsAP._mute = True
			self.trimAdsPlaybackMpegReaderTracks[0].set_observer(self.display_ads_trimmed_frame_till_end)
		else:

			pixBuf = gtk.gdk.pixbuf_new_from_array(thearray, gtk.gdk.COLORSPACE_RGB, 8) 
			self.mainNotebookImagePlayback.set_from_pixbuf(pixBuf)
                	self.mainNotebookImagePlayback.queue_draw()
		return

    	def display_ads_trimmed_frame_till_end(self,thearray):
      		"""
      		pyffmpeg callback

      		"""
		computedHash = self.computeHash(thearray)
		if computedHash in self.adDictionaryFileEndFrame:
			print "Found matching ad end ", self.adDictionaryFileEndFrame[computedHash]
			im = Image.fromarray(thearray)
			im.save("end.jpg", "jpeg")

			im = Image.fromarray(thearray)
			self.trimAdsDisplayBeginReInit = True
			self.trimAdsPlaybackMpegReaderTracks[0].set_observer(self.display_ads_trimmed_frame_till_begin)
			self.trimAdsAP._mute = False

	def display_no_op(self, thearray):
		print "in display no op"
		return

	def on_button_stop_clicked(self, widget):
		# Remove timers for playback and trim Ads
		if not (self.playbackTimer == None) :
			gobject.source_remove(self.playbackTimer)
  	        	self.playbackTimer = None
		if not (self.trimAdsPlaybackTimer == None) :
			gobject.source_remove(self.trimAdsPlaybackTimer)
			self.trimAdsPlaybackTimer = None
		# Remove reader objects for playback and trim Ads
		if not (self.playbackMpegReader == None):
			del self.playbackMpegReader
			self.playbackMpegReader =None
		if not (self.trimAdsPlaybackMpegReader == None):
			del self.trimAdsPlaybackMpegReader
			self.trimAdsPlaybackMpegReader =None
		# Initialize playback scale to 0
		self.scale.set_value(0)
		self.timeLabel.set_text("00:00:00")
		return

	def on_button_kmeans_clicked(self, widget):
		if (self.mp == None):
			## create the reader object
			self.mp=FFMpegReader()

			## open an audio video file
			self.mp.open(self.currentFileSelectedFullPathName, TS_VIDEO_RGB24)
			self.tracks=self.mp.get_tracks()

			## connect audio to its device
			self.ap=AlsaSoundLazyPlayer(self.tracks[1].get_samplerate(),self.tracks[1].get_channels(),int(self.tracks[0].get_fps()))
			self.tracks[1].set_observer(self.ap.push_nowait)
			self.tracks[0].set_observer(self.displayKMeansFrame)
		self.mp.step()

		return 
		

	def displayKMeansFrame(self, thearray):
      		"""
      		pyffmpeg callback
      		"""

	
                im = adaptors.NumPy2Ipl(thearray)
                K = int(sys.argv[1])

                # Prepare the data for K-means.  Represent each pixel in the image as a 3D
                # vector (each dimension corresponds to one of B,G,R color channel value).
                # Create a column of such vectors -- it will be width*height tall, 1 wide
                # and have a total 3 channels.
                #
                col = cvReshape(im, 3, im.width*im.height)
                samples = cvCreateMat(col.height, 1, CV_32FC3)
                cvConvertScale(col, samples)
                labels = cvCreateMat(col.height, 1, CV_32SC1)
                #
                # Run 10 iterations of the K-means algorithm.
                #
                crit = (CV_TERMCRIT_EPS + CV_TERMCRIT_ITER, 10, 1.0)
                cvKMeans2(samples, K, labels, crit)
		
		#create the pixBuf

		pixBuf = gtk.gdk.pixbuf_new_from_array(thearray, gtk.gdk.COLORSPACE_RGB, 8) 

		#demarcate kmeans boundary
		pixelarr = pixBuf.get_pixels_array()
		currClusterNum = -1
		oldClusterNum = -1
		pixBufHeight = pixBuf.get_height()
		pixBufWidth = pixBuf.get_width()
		for y in range(pixBufHeight):
    			for x in range(pixBufWidth):
				currClusterNum = labels[y*pixBufWidth + x]
				if (not(oldClusterNum == currClusterNum)):
        				pixelarr[y, x] = 0
					oldClusterNum = currClusterNum
			
		currClusterNum = -1
		oldClusterNum = -1
		for y in range(pixBufWidth):
    			for x in range(pixBufHeight):
				currClusterNum = labels[x*pixBufWidth + y]
				if (not(oldClusterNum == currClusterNum)):
        				pixelarr[x, y] = 0
					oldClusterNum = currClusterNum
		pixBufNew = gtk.gdk.pixbuf_new_from_array(pixelarr, gtk.gdk.COLORSPACE_RGB, 8) 
			
		self.mainNotebookImagePlayback.set_from_pixbuf(pixBufNew)
                self.mainNotebookImagePlayback.queue_draw()
		return

	
	def on_MainNotebook_switch_page(self, widget, page, page_num):
		if (page_num == 2):
			# We are in the compose tab 
			self.hboxPlayBack.hide()
			self.hboxEdit.hide()
			self.hboxCompose.show()
		if (page_num == 1):
			# We are in the edit tab 
			self.hboxPlayBack.hide()
			self.hboxCompose.hide()
			self.hboxEdit.show()
		elif (page_num == 0):
			# We are in the playback tab
			self.hboxPlayBack.show()
			self.hboxCompose.hide()
			self.hboxEdit.hide()
		return	


	def on_MainNotebook_switch_page_algo (self, widget, page, page_num):
		# We are in the edit tab => populate the list store and the icon view widgets 
		if (page_num == 1):
			#Call the algorithm for determining POI*/
			numThumbnails = self.one_pass_algo(self.currentFileSelectedFullPathName)
			if (numThumbnails > 0):
				editThumbnailsListStore =  gtk.ListStore (gtk.gdk.Pixbuf)
				editThumbnailsIconView = gtk.IconView(editThumbnailsListStore)
				editThumbnailsIconView.set_pixbuf_column(0)
				#Read the frames one by one and populate the list store */
				for i in range(0, numThumbnails):
					i = i + 1
					FirstPassPOIFileName =  "POI-TP-" + str(i) + ".jpeg"
  					pixbuf = gtk.gdk.pixbuf_new_from_file(FirstPassPOIFileName)
					editThumbnailsListStore.append((pixbuf,))
				self.mainNotebookEditScrolledWindow.add(editThumbnailsIconView)
		self.window.show_all()
		return

	def on_scale_change_value (self, widget, scroll, value):
		self.playbackTimeInSecondsFromScale = int(value)
		self.currFilePlaybackNewTimeInHHMMSS = time.strftime('%H:%M:%S', time.gmtime(self.playbackTimeInSecondsFromScale))
		self.timeLabel.set_text(self.currFilePlaybackNewTimeInHHMMSS)
		if not (self.playbackTimer == None) :
			gobject.source_remove(self.playbackTimer)
  	        	self.playbackTimer = None
		if not (self.trimAdsPlaybackTimer == None) :
			gobject.source_remove(self.trimAdsPlaybackTimer)
  	        	self.trimAdsPlaybackTimer = None
		if self.playbackMode:
			if not(self.playbackMpegReader == None):
				del self.playbackMpegReader
			self.playbackMpegReader=FFMpegReader()
			self.playbackMpegReader.open(self.currentFileSelectedFullPathName, TS_VIDEO_RGB24)
			self.playbackMpegReaderTracks=self.playbackMpegReader.get_tracks()

			## connect video to its device
			self.playbackMpegReaderTracks[0].set_observer(self.displayFrameScaleChange)
			self.playbackMpegReaderTracks[0].seek_to_seconds(self.playbackTimeInSecondsFromScale)
			self.playbackMpegReader.step()
				
			del self.playbackMpegReader
			self.playbackMpegReader = None
		
		mouse_x, mouse_y =  widget.get_pointer()
		print mouse_x, mouse_y
						

		return	

	def displayFrameScaleChange(self, thearray):
		pixBuf = gtk.gdk.pixbuf_new_from_array(thearray, gtk.gdk.COLORSPACE_RGB, 8) 
		self.mainNotebookImagePlayback.set_from_pixbuf(pixBuf)
                self.mainNotebookImagePlayback.queue_draw()
		return 
		
	def on_button_pause_clicked(self,widget):
		self.playbackPaused = True
		if not (self.playbackTimer == None) :
			gobject.source_remove(self.playbackTimer)
  	        	self.playbackTimer = None
		if not (self.trimAdsPlaybackTimer == None) :
			gobject.source_remove(self.trimAdsPlaybackTimer)
  	        	self.trimAdsPlaybackTimer = None
		return


	def on_scale_motion_notify_event(self, widget, event):
		return

	def on_button_in_clicked (self, widget):
		scaleValue = self.scale.get_value()
		mouse_x, mouse_y = self.scale.get_pointer()
		inArrow = gtk.Arrow(gtk.ARROW_UP, gtk.SHADOW_NONE)
		inArrow.queue_draw_area(mouse_x, mouse_y, 10, 10)
		self.hboxEditArrow.add(inArrow)
		inArrow.show()
		self.scale.add_mark(scaleValue, gtk.POS_BOTTOM, None)
		return
			
		
	def on_button_out_clicked (self, widget):
		scaleValue = self.scale.get_value()
		mouse_x, mouse_y = self.scale.get_pointer()
		self.scale.add_mark(scaleValue, gtk.POS_BOTTOM, None)
		return


	def on_button_compose_pane_vbox_add_clicked (self, widget):
		self.fileChooserDialog = gtk.FileChooserDialog(title=None,action=gtk.FILE_CHOOSER_ACTION_OPEN,
                                  buttons=(gtk.STOCK_CANCEL,gtk.RESPONSE_CANCEL,gtk.STOCK_OPEN,gtk.RESPONSE_OK))
		self.fileChooserDialogResponse=self.fileChooserDialog.run()
		if self.fileChooserDialogResponse == gtk.RESPONSE_OK:	
			self.currentComposeFileSelectedFullPathName = self.fileChooserDialog.get_filename()
			#extract the first frame from the video and add a thumbnail
			self.composeFFMpegReader = FFMpegReader()
			self.composeFFMpegReader.open(self.currentComposeFileSelectedFullPathName)
			self.composeFFMpegReaderTracks = self.composeFFMpegReader.get_tracks()
			self.composeFFMpegReaderTracks[0].set_observer(self.initialize_compose_frame)
			try:
				self.composeFFMpegReader.step()
			except IOError:
				del self.composeFFMpegReader
			del self.composeFFMpegReader
		self.fileChooserDialog.destroy()
		return

	def initialize_compose_frame(self, thearray):
		#check if the init MainNotbookComposeVBoxImage exists and remove the default image
		if not(self.mainNotebookComposeVBoxImage == None):
			self.mainNotebookComposeVBox.remove(self.mainNotebookComposeVBoxImage)
			self.mainNotebookComposeVBoxImage == None
		
		#Init a scrolled window
		self.mainNotebookComposeVBoxScrolledWindow = gtk.ScrolledWindow()
		self.mainNotebookComposeVBoxScrolledWindow.set_policy(gtk.POLICY_AUTOMATIC, gtk.POLICY_AUTOMATIC)


		#Initialize an icon view and add to the scrolled window
		self.mainNotebookComposeVBoxIconView = gtk.IconView()
    		self.mainNotebookComposeVBoxListStore = gtk.ListStore(gtk.gdk.Pixbuf, str)
    		self.mainNotebookComposeVBoxIconView.set_model(self.mainNotebookComposeVBoxListStore)
    		self.mainNotebookComposeVBoxIconView.set_pixbuf_column(0)
    		self.mainNotebookComposeVBoxIconView.set_text_column(1)
    		self.mainNotebookComposeVBoxIconView.set_columns(2)
		self.mainNotebookComposeVBoxScrolledWindow.add_with_viewport(self.mainNotebookComposeVBoxIconView)
		self.mainNotebookComposeVBox.pack_start(self.mainNotebookComposeVBoxScrolledWindow, True, True, 10 )

		#make an image with the current frame and add to the model
		pixBuf = gtk.gdk.pixbuf_new_from_array(thearray, gtk.gdk.COLORSPACE_RGB, 8) 
		pixBufScaled =  pixBuf.scale_simple(120, 100, gtk.gdk.INTERP_HYPER)
		self.mainNotebookComposeVBoxListStore.append((pixBufScaled,self.currentComposeFileSelectedFullPathName))

		numComposeVBoxChildren = self.mainNotebookComposeVBox.get_children()
		newAddButtonPos = len(numComposeVBoxChildren)
		self.mainNotebookComposeVBox.reorder_child(self.buttonComposePaneVBoxAdd, newAddButtonPos)
		self.mainNotebookComposeVBox.show_all()
		
		
		
		return

	def on_button_add_clicked (self, widget):
		return

	def on_button_export_clicked (self, widget):
		return

	def on_button_save_trim_ads_clicked(self, widget):
		self.saveTrimAdsFileChooserDialog = gtk.FileChooserDialog(title=None,action=gtk.FILE_CHOOSER_ACTION_SAVE,
                                  buttons=(gtk.STOCK_CANCEL,gtk.RESPONSE_CANCEL,gtk.STOCK_SAVE,gtk.RESPONSE_OK))
                self.saveTrimAdsFileChooserDialogResponse=self.saveTrimAdsFileChooserDialog.run()
                if self.saveTrimAdsFileChooserDialogResponse == gtk.RESPONSE_OK:
                        self.currentSaveTrimAdsFileSelectedFullPathName = self.saveTrimAdsFileChooserDialog.get_filename()
			#Convert the file at a constant bit rate to mpg
			ffmpegConvertToMpgString = 'ffmpeg -i ' + self.currentFileSelectedFullPathName + ' -b 2250k -minrate 2250k -maxrate 2250k -bufsize 1000k temp.mpg'
			os.system(ffmpegConvertToMpgString)
			
			#Get the ranges for splits after trimming ads
			videoCaptureFile = cvCreateFileCapture(self.currentFileSelectedFullPathName);
			self.saveTrimAdsCurrFilePlaybackFps =  int(cvGetCaptureProperty( videoCaptureFile, CV_CAP_PROP_FPS))
			self.saveTrimAdsCurrFilePlaybackNFrames =  int(cvGetCaptureProperty( videoCaptureFile, CV_CAP_PROP_FRAME_COUNT ))
			cvReleaseCapture(videoCaptureFile)
			self.saveTrimAdsCurrFilePlaybackFrameNum = 0
			self.saveTrimAdsCurrFilePlaybackCurrTimeInSeconds = 0
			self.saveTrimAdsCurrFilePlaybackTotalTimeInSeconds = int(self.saveTrimAdsCurrFilePlaybackNFrames/self.saveTrimAdsCurrFilePlaybackFps)
			self.saveTrimAdsMpegReader = FFMpegReader()
			self.saveTrimAdsMpegReader.open(self.currentFileSelectedFullPathName)
			self.saveTrimAdsTracks = self.saveTrimAdsMpegReader.get_tracks()
			self.saveTrimAdsRanges = []
			self.saveTrimAdsCurrRangeBegin = 0.00
			self.saveTrimAdsSkippingAd = False
			self.saveTrimAdsFirstFrameIsAd = False
			self.saveTrimAdsTracks[0].set_observer(self.saveTrimAdsGetRangeEnd)
			while True:
				try:
					self.saveTrimAdsMpegReader.step()
				except IOError:
					break;
				
			del self.saveTrimAdsMpegReader
			self.saveTrimAdsMpegReader = None

			#add a last range
			lastRange = "[" + self.time_in_seconds_to_hh_mm_ss_ss(self.saveTrimAdsCurrRangeBegin) + "-]"
			self.saveTrimAdsRanges.append(lastRange)


			#Use mpgtx to split the file with ranges
			mpgtxTrimString = 'mpgtx -j temp.mpg '
			
			for i in range(0, len(self.saveTrimAdsRanges)):
				mpgtxTrimString  = mpgtxTrimString +  " " + self.saveTrimAdsRanges[i] + " " 
			mpgtxTrimString = mpgtxTrimString  + ' -o out.mpg '
			print "will execute " + mpgtxTrimString
			os.system(mpgtxTrimString)

			#Transcode mpg back to the format specified at save time
			ffmpegTranscodeToOutputString = 'ffmpeg -i out.mpg ' + self.currentSaveTrimAdsFileSelectedFullPathName 
			os.system(ffmpegTranscodeToOutputString)
			
			#cleanup
			os.remove("temp.mpg")
			os.remove("out.mpg")

                self.saveTrimAdsFileChooserDialog.destroy()

	def saveTrimAdsGetRangeEnd(self, thearray):
		self.saveTrimAdsCurrFilePlaybackFrameNum = self.saveTrimAdsCurrFilePlaybackFrameNum + 1
		self.saveTrimAdsCurrFilePlaybackCurrTimeInSeconds = float(self.saveTrimAdsCurrFilePlaybackFrameNum)/float(self.saveTrimAdsCurrFilePlaybackFps)
		self.saveTrimAdsCurrFilePlaybackCurrTimeInSeconds = round(self.saveTrimAdsCurrFilePlaybackCurrTimeInSeconds,2)
		if not (self.saveTrimAdsSkippingAd):
			computedHash = self.computeHash(thearray)
	
			#see if we can match an ad
			if (computedHash in self.adDictionaryFileNames):
				#skip the number of frames in the ad
				self.saveTrimAdsSkippingAd = True
				for i in range(1, self.currAdFramesToSkip - self.currAdFrameNumberMatched):
					try:
						self.saveTrimAdsMpegReader.step()
					except IOError:
						return
				self.saveTrimAdsSkippingAd = False
		return 

	def time_in_seconds_to_hh_mm_ss_ss(self, timeIn):
		milliseconds = timeIn * 1000
		hours, milliseconds = divmod(milliseconds, 3600000)
		minutes, milliseconds = divmod(milliseconds, 60000)
		seconds = float(milliseconds)/ 1000
		retVal = "%02i:%02i:%05.2f" % (hours, minutes, seconds)
		return retVal
		

	def main(self):
		try:
			gtk.main()
		except Exception, e:
			print  "Got an exception ", e
			#do clean up
			os.remove("temp.mpg")
			os.remove("out.mpg")

if __name__ == "__main__":
	vEditor = VideoEditor()
	vEditor.main()
