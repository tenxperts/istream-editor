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

import time
import redis_wrap
import redis
import os

TS_VIDEO_RGB24={ 'video1':(0, -1, {'pixel_format':PixelFormats.RGB24}), 'audio1':(1,-1,{})}


class VideoEditor:

	def __init__(self):

		self.adDictionaryFileNames = redis_wrap.get_hash('adDictionaryFileNames')
		self.adDictionaryFileTotalFrames = redis_wrap.get_hash('adDictionaryFileTotalFrames')
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


	def compute_ad_frame_hash(self, thearray):
		computedHash = self.computeHash(thearray)
		videoCaptureFile = cvCreateFileCapture(self.currentAdSelectedFullPathName);
		nFrames =  int(cvGetCaptureProperty( videoCaptureFile, CV_CAP_PROP_FRAME_COUNT ))
		self.adDictionaryFileNames[computedHash] = self.currentAdSelectedFullPathName
		self.adDictionaryFileTotalFrames[computedHash] = nFrames-1
		cvReleaseCapture(videoCaptureFile)
		return
		

	def main(self):
		try:
			gtk.main()
		except Exception, e:
			print  "Got an exception ", e
			#do clean up
			os.remove("temp.mpg")

if __name__ == "__main__":
	vEditor = VideoEditor()
	vEditor.main()
