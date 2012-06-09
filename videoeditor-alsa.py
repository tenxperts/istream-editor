#!/usr/bin/env python
"""This is a Py GTK Glade based video editor. Author - Anshuman Rai 22 Feb 2012"""

import sys 
from opencv.cv import *
from opencv.highgui import *
import gobject

from pyffmpeg import *

import alsaaudio
from opencv import adaptors

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
    def push_nowait(self,stamped_buffer):
        self._d.write(stamped_buffer[0].data)

class VideoEditor:

	def __init__(self):
		
		self.gladeFile = "videoeditor.xml"
        	self.builder = gtk.Builder()
        	self.builder.add_from_file(self.gladeFile)

		self.window = self.builder.get_object("MainWindow")
		self.ad_dictionary = {}
		self.mainFrameImage = self.builder.get_object("MainFrameImage")
		self.mainNotebookImagePlayback = self.builder.get_object("MainNotebookImagePlayback")
		self.mainNotebookEditScrolledWindow = self.builder.get_object("MainNotebookEditScrolledWindow")
		self.frameRGB = None
    		self.snd=None
		self.mp=None
		self.tracks=None
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
	


	def one_pass_algo(self, filename):
		import os
		system_cmd_string = './algo ' + filename + ' 2>/dev/null'
		os.system(system_cmd_string)
		algo_output_file = open('algo.out')
		retval = int(algo_output_file.read(4))
		algo_output_file.close()
		return retval

	def main_menu_bar_file_open_activate(self, widget):		
		self.file_open_mode = True
		self.ad_load_mode = False
		self.fileChooserDialog = gtk.FileChooserDialog(title=None,action=gtk.FILE_CHOOSER_ACTION_OPEN,
                                  buttons=(gtk.STOCK_CANCEL,gtk.RESPONSE_CANCEL,gtk.STOCK_OPEN,gtk.RESPONSE_OK))
		self.fileChooserDialogResponse=self.fileChooserDialog.run()
		if self.fileChooserDialogResponse == gtk.RESPONSE_OK:	
			self.currentFileSelectedFullPathName = self.fileChooserDialog.get_filename()
		self.fileChooserDialog.destroy()
		return	

	def main_menu_bar_ad_load_activate(self, widget):
		self.ad_load_mode = True
		self.file_open_mode = False
		self.fileChooserDialog = gtk.FileChooserDialog(title=None,action=gtk.FILE_CHOOSER_ACTION_OPEN,
                                  buttons=(gtk.STOCK_CANCEL,gtk.RESPONSE_CANCEL,gtk.STOCK_OPEN,gtk.RESPONSE_OK))
		self.fileChooserDialogResponse = self.fileChooserDialog.run()
		if self.fileChooserDialogResponse== gtk.RESPONSE_OK : 
			self.currentAdSelectedFullPathName = self.fileChooserDialog.get_filename()
			self.processAdLoad()
		self.fileChooserDialog.destroy()
		return	

	def computeHash(self,frame):
		im = adaptors.Ipl2PIL(frame)
    		im = im.resize((8, 8), Image.ANTIALIAS).convert('L')
    		avg = reduce(lambda x, y: x + y, im.getdata()) / 64.
    		return reduce(lambda x, (y, z): x | (z << y), enumerate(map(lambda i: 0 if i < avg else 1, im.getdata())), 0)

	def hamming(self, h1, h2):
     		h, d = 0, h1 ^ h2
     		while d:
         		h += 1
         		d &= d - 1
     		return h

	def processAdLoad(self):
		videoCaptureFile = cvCreateFileCapture(self.currentAdSelectedFullPathName);

		nFrames =  cvGetCaptureProperty( videoCaptureFile, CV_CAP_PROP_FRAME_COUNT )
		fps =  int(cvGetCaptureProperty( videoCaptureFile, CV_CAP_PROP_FPS))
		for i in range(1,fps):
                	frame = cvQueryFrame(videoCaptureFile)
			computedHash = self.computeHash(frame)
			self.ad_dictionary[computedHash] = (self.currentAdSelectedFullPathName, nFrames-1)
		cvReleaseCapture(videoCaptureFile)
		return

	def on_button_trim_ads_clicked(self, widget):
		videoCaptureFile = cvCreateFileCapture(self.currentFileSelectedFullPathName);
		gobject.timeout_add(30, self.trim_ads_video_playback_handler,videoCaptureFile)
		gobject.timeout_add(30, self.trim_ads_audio_playback_handler)
		return

		frame = cvQueryFrame(capture)
        	if (frame == None):
        		cvReleaseCapture(capture)
			return 0
		self.frameRGB = cvCreateImage(cvSize(frame.width, frame.height), frame.depth, frame.nChannels) ;
		cvCvtColor( frame, self.frameRGB, CV_BGR2RGB ); 
		#Usually opencv image is BGR, so we need to change it to RGB 
		pixBuf = gtk.gdk.pixbuf_new_from_data(self.frameRGB.imageData, gtk.gdk.COLORSPACE_RGB, 0, 8, self.frameRGB.width, self.frameRGB.height, self.frameRGB.widthStep)
		self.mainNotebookImagePlayback.set_from_pixbuf(pixBuf)
		self.mainNotebookImagePlayback.queue_draw()
		return 1

	def trim_ads_audio_playback_handler(self):
		if (self.mp == None):
			## create the reader object
			self.mp=FFMpegReader()
			## open an audio video file
			filenamearr = self.currentFileSelectedFullPathName.split(".")
			self.mp.open(filenamearr[0] + "-copy." + filenamearr[1], TS_VIDEO_RGB24)
			self.tracks=self.mp.get_tracks()

			## connect audio to its device

			self.ap=AlsaSoundLazyPlayer(self.tracks[1].get_samplerate(),self.tracks[1].get_channels(),self.tracks[0].get_fps())

			self.tracks[1].set_observer(self.ap.push_nowait)
		self.mp.step()
		return 1

	def on_button_kmeans_clicked(self, widget):
		return

	def on_button_play_clicked(self, widget):
        	videoCaptureFile = cvCreateFileCapture(self.currentFileSelectedFullPathName);
		gobject.timeout_add(30, self.video_playback_handler, videoCaptureFile)	
		gobject.timeout_add(30, self.audio_playback_handler)	
		return

	def audio_playback_handler(self):
		if (self.mp == None):
			## create the reader object
			self.mp=FFMpegReader()
			## open an audio video file
			filenamearr = self.currentFileSelectedFullPathName.split(".")
			self.mp.open(filenamearr[0] + "-copy." + filenamearr[1], TS_VIDEO_RGB24)
			self.tracks=self.mp.get_tracks()

			## connect audio to its device

			self.ap=AlsaSoundLazyPlayer(self.tracks[1].get_samplerate(),self.tracks[1].get_channels(),self.tracks[0].get_fps())

			self.tracks[1].set_observer(self.ap.push_nowait)
		self.mp.step()
		return 1


	def trim_ads_video_playback_handler(self, capture):
		frame = cvQueryFrame(capture)
		computedHash = self.computeHash(frame)
		if (self.ad_dictionary.has_key(computedHash)):
			(self.curr_ad_match_name, self.curr_ad_frames_to_skip) = self.ad_dictionary[computedHash] 
			print "Found matching ad " + self.curr_ad_match_name
			print "Will skip ", self.curr_ad_frames_to_skip, " frames "
			while not(self.curr_ad_frames_to_skip == 0):
				frame = cvQueryFrame(capture)
				self.curr_ad_frames_to_skip = self.curr_ad_frames_to_skip - 1

        	if (frame == None):
        		cvReleaseCapture(capture)
			return 0
		self.frameRGB = cvCreateImage(cvSize(frame.width, frame.height), frame.depth, frame.nChannels) ;
		cvCvtColor( frame, self.frameRGB, CV_BGR2RGB ); 
		#Usually opencv image is BGR, so we need to change it to RGB 
		pixBuf = gtk.gdk.pixbuf_new_from_data(self.frameRGB.imageData, gtk.gdk.COLORSPACE_RGB, 0, 8, self.frameRGB.width, self.frameRGB.height, self.frameRGB.widthStep) 
		self.mainNotebookImagePlayback.set_from_pixbuf(pixBuf)
		self.mainNotebookImagePlayback.queue_draw()
		return 1
		

	def on_button_stop_clicked(self, widget):
		return

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
