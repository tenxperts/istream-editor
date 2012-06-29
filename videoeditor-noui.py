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
		self.currFilePlaybackFrameNum = 0
		self.currFilePlaybackCurrTimeInSeconds = 0
		self.currFilePlaybackTotalTimeInSeconds = 0
		self.saveTrimAdsMpegReader = None
		return

	def main_menu_bar_file_open_activate(self, widget):
		self.fileChooserDialog = gtk.FileChooserDialog(title=None,action=gtk.FILE_CHOOSER_ACTION_OPEN,
                                  buttons=(gtk.STOCK_CANCEL,gtk.RESPONSE_CANCEL,gtk.STOCK_OPEN,gtk.RESPONSE_OK))
		self.fileChooserDialogResponse=self.fileChooserDialog.run()
		if self.fileChooserDialogResponse == gtk.RESPONSE_OK:	
			self.currentFileSelectedFullPathName = self.fileChooserDialog.get_filename()
		self.fileChooserDialog.destroy()
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
			self.saveTrimAdsCurrFilePlaybackFrameNum = 0
			self.saveTrimAdsCurrFilePlaybackCurrTimeInSeconds = 0
			self.saveTrimAdsCurrFilePlaybackTotalTimeInSeconds = int(self.saveTrimAdsCurrFilePlaybackNFrames/self.saveTrimAdsCurrFilePlaybackFps)
			cvReleaseCapture(videoCaptureFile)
			self.saveTrimAdsMpegReader = FFMpegReader()
			self.saveTrimAdsMpegReader.open(self.currentFileSelectedFullPathName)
			self.saveTrimAdsTracks = self.saveTrimAdsMpegReader.get_tracks()
			self.saveTrimAdsRanges = []
			self.saveTrimAdsCurrRangeBegin = 0
			self.saveTrimAdsSkippingAd = False
			self.saveTrimAdsTracks[0].set_observer(self.saveTrimAdsGetRanges)
			while True:
				try:
					self.saveTrimAdsMpegReader.step()
				except IOError:
					break;
				
			del self.saveTrimAdsMpegReader
			self.saveTrimAdsMpegReader = None

			#add a last range
			lastRange = "[0:" + str(self.saveTrimAdsCurrRangeBegin) + "-]"
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
			#os.remove("out.mpg")

                self.saveTrimAdsFileChooserDialog.destroy()

	def saveTrimAdsGetRanges(self, thearray):
		self.saveTrimAdsCurrFilePlaybackFrameNum = self.saveTrimAdsCurrFilePlaybackFrameNum + 1
		self.saveTrimAdsCurrFilePlaybackCurrTimeInSeconds = int(self.saveTrimAdsCurrFilePlaybackFrameNum/self.saveTrimAdsCurrFilePlaybackFps)
		if not (self.saveTrimAdsSkippingAd):
			computedHash = self.computeHash(thearray)
	
			#see if we can match an ad	
			if (computedHash in self.adDictionaryFileNames):
				self.currAdMatchName =  self.adDictionaryFileNames[computedHash]
				self.currAdFramesToSkip= int(self.adDictionaryFileTotalFrames[computedHash])
				print "save trim ads found matching ad " + self.currAdMatchName
				#Add a range
				if len (self.saveTrimAdsRanges) == 0:
					if not (self.saveTrimAdsCurrFilePlaybackCurrTimeInSeconds == 0):
						currRange = "[-0:" + str(self.saveTrimAdsCurrFilePlaybackCurrTimeInSeconds) + "]"
					else:
						currRange = "[-0:1]"  
						
					self.saveTrimAdsRanges.append(currRange)
				else:
					if not (self.saveTrimAdsCurrFilePlaybackCurrTimeInSeconds == self.saveTrimAdsCurrRangeBegin):
						currRange = "[0:" + str(self.saveTrimAdsCurrRangeBegin) + "-0:" + str(self.saveTrimAdsCurrFilePlaybackCurrTimeInSeconds) + "]"
					else:
						currRange = "[0:" + str(self.saveTrimAdsCurrRangeBegin) + "-0:" + str(self.saveTrimAdsCurrFilePlaybackCurrTimeInSeconds + 1) + "]"
					self.saveTrimAdsRanges.append(currRange)
				#compute the begin time for the next range
				self.saveTrimAdsCurrRangeBegin = int ((self.saveTrimAdsCurrFilePlaybackFrameNum + self.currAdFramesToSkip) / self.saveTrimAdsCurrFilePlaybackFps) 
				#skip the number of frames in the ad
				self.saveTrimAdsSkippingAd = True
				for i in range(1, self.currAdFramesToSkip):
					try:
						self.saveTrimAdsMpegReader.step()
					except IOError:
						return
				self.saveTrimAdsSkippingAd = False
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
