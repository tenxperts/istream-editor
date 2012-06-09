#!/usr/bin/env python
"""This is a Py GTK Glade based video editor. Author - Anshuman Rai 22 Feb 2012"""

import sys 
from opencv.cv import *
from opencv.highgui import *
from opencv import adaptors
import gobject
import cv


#Anshuman :added on 28 May 2012 : sha1 hash imports

from hashlib import sha1


import numpy


from pyffmpeg import *

import alsaaudio

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


		self.adDictionary = {}
		self.window = self.builder.get_object("MainWindow")
		self.mainFrameImage = self.builder.get_object("MainFrameImage")
		self.mainNotebookImagePlayback = self.builder.get_object("MainNotebookImagePlayback")
		self.mainNotebookEditScrolledWindow = self.builder.get_object("MainNotebookEditScrolledWindow")
		self.frameRGB = None
    		self.snd=None
		self.playbackMpegReader = None
		self.playbackMpegReaderTracks = None
		self.adLoadMpegReader = None
		self.adLoadMpegReaderTracks = None
		self.trimAdsPlaybackMpegReader = None
		self.trimAdsPlaybackMpegReaderTracks = None
		self.skipAdFrames = False
		self.currAdFramesToSkip = 0
		if (self.window):
			dic = { "on_MainWindow_destroy" : gtk.main_quit,
				"on_MainMenuBar_file_open_activate" : self.main_menu_bar_file_open_activate,
				"on_MainMenuBar_ad_load_activate" : self.main_menu_bar_ad_load_activate,
				"on_buttonPlay_clicked" : self.on_button_play_clicked,
				"on_buttonStop_clicked" : self.on_button_stop_clicked,
				"on_buttonKMeans_clicked" : self.on_button_kmeans_clicked,
				"on_buttonTrimAds_clicked" : self.on_button_trim_ads_clicked,
				"on_MainNotebook_switch_page" : self.on_MainNotebook_switch_page}
			self.builder.connect_signals(dic)
			self.window.show()
		return
	

    	def displayframe(self,thearray):
      		"""
      		pyffmpeg callback
      		"""

		pixBuf = gtk.gdk.pixbuf_new_from_array(thearray, gtk.gdk.COLORSPACE_RGB, 8) 
		self.mainNotebookImagePlayback.set_from_pixbuf(pixBuf)
                self.mainNotebookImagePlayback.queue_draw()
		return

		
	def one_pass_algo(self, filename):
		import os
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

	

	def processAdLoad(self):
                if (self.adLoadMpegReader == None):
                        ## create the reader object
                        self.adLoadMpegReader=FFMpegReader()

                	## open an audio video file
                	self.adLoadMpegReader.open(self.currentAdSelectedFullPathName, TS_VIDEO_RGB24)
                	self.adLoadMpegReaderTracks=self.adLoadMpegReader.get_tracks()

                	self.adLoadMpegReaderTracks[0].set_observer(self.compute_ad_frame_hash)
		videoCaptureFile = cvCreateFileCapture(self.currentAdSelectedFullPathName);
		fps =  int(cvGetCaptureProperty( videoCaptureFile, CV_CAP_PROP_FPS))
		for i in range(1,fps):
                	self.adLoadMpegReader.step()
		cvReleaseCapture(videoCaptureFile)
		del self.adLoadMpegReader
		self.adLoadMpegReader = None
		return

	def computeHash(self,frame):
		im = adaptors.NumPy2PIL(frame)
    		im = im.resize((8, 8), Image.ANTIALIAS).convert('L')
    		avg = reduce(lambda x, y: x + y, im.getdata()) / 64.
    		return reduce(lambda x, (y, z): x | (z << y), enumerate(map(lambda i: 0 if i < avg else 1, im.getdata())), 0)

	def hamming(self, h1, h2):
     		h, d = 0, h1 ^ h2
     		while d:
         		h += 1
         		d &= d - 1
     		return h

	def compute_ad_frame_hash(self, thearray):
		computedHash = self.computeHash(thearray)
		videoCaptureFile = cvCreateFileCapture(self.currentAdSelectedFullPathName);
		nFrames =  int(cvGetCaptureProperty( videoCaptureFile, CV_CAP_PROP_FRAME_COUNT ))
		self.adDictionary[computedHash] = (self.currentAdSelectedFullPathName, nFrames-1)
		cvReleaseCapture(videoCaptureFile)
		return
		
	def on_button_play_clicked(self, widget):
		gobject.timeout_add(30, self.playback_handler)


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
			self.playbackMpegReader.step()
			return 1
		except:
			del playbackMpegReader
			return 0

	def on_button_trim_ads_clicked(self, widget):
		gobject.timeout_add(30, self.trim_ads_playback_handler)
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
			self.trimAdsPlaybackMpegReaderTracks[0].set_observer(self.display_ads_trimmed_frame)
			return 1
		self.trimAdsPlaybackMpegReader.step()
		return 1


    	def display_ads_trimmed_frame(self,thearray):
      		"""
      		pyffmpeg callback
      		"""
		if not self.skipAdFrames:
			computedHash = self.computeHash(thearray)
		
			if (self.adDictionary.has_key(computedHash)):
				(self.currAdMatchName, self.currAdFramesToSkip) = self.adDictionary[computedHash] 
				print "Found matching ad " , self.currAdMatchName, " will skip ", self.currAdFramesToSkip, " frames "
				self.skipAdFrames = True
				self.trimAdsAP._mute = True
				for i in range (1,self.currAdFramesToSkip):
					self.trimAdsPlaybackMpegReader.step()
				self.skipAdFrames = False
				self.trimAdsAP._mute = False

		pixBuf = gtk.gdk.pixbuf_new_from_array(thearray, gtk.gdk.COLORSPACE_RGB, 8) 
		self.mainNotebookImagePlayback.set_from_pixbuf(pixBuf)
                self.mainNotebookImagePlayback.queue_draw()
		return


	def on_button_stop_clicked(self, widget):
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

		


	def on_MainNotebook_switch_page (self, widget, page, page_num):
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


	def main(self):
		gtk.main()

if __name__ == "__main__":
	vEditor = VideoEditor()
	vEditor.main()
