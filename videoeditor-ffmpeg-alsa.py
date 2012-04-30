#!/usr/bin/env python
"""This is a Py GTK Glade based video editor. Author - Anshuman Rai 22 Feb 2012"""

import sys 
from opencv.cv import *
from opencv.highgui import *
import gobject


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
        self._d.setperiodsize((rate*channels)//fps)
        self._d.setrate(rate)
    def push_nowait(self,stamped_buffer):
        self._d.write(stamped_buffer[0].data)


class VideoEditor:

	def __init__(self):
		
		self.gladeFile = "videoeditor.xml"
        	self.builder = gtk.Builder()
        	self.builder.add_from_file(self.gladeFile)

		self.window = self.builder.get_object("MainWindow")
		self.fileChooserDialog = self.builder.get_object("FileChooserDialog")
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
				"on_FileChooserDialog_file_activated" : self.file_chooser_dialog_file_activated,
				"on_buttonPlay_clicked" : self.on_button_play_clicked,
				"on_buttonStop_activate" : self.on_button_stop_clicked,
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


	def one_pass_algo(self, filename):
		import os
		system_cmd_string = './algo ' + filename + ' 2>/dev/null'
		os.system(system_cmd_string)
		algo_output_file = open('algo.out')
		retval = int(algo_output_file.read(4))
		algo_output_file.close()
		return retval

	def main_menu_bar_file_open_activate(self, widget):
		self.fileChooserDialog.show()
		return	

	def file_chooser_dialog_file_activated(self, widget):
		self.fileChooserDialog.hide()
		self.currentFileSelectedFullPathName = self.fileChooserDialog.get_filename()
		return	


	def on_button_play_clicked(self, widget):
		gobject.timeout_add(30, self.playback_handler)

	def playback_handler(self):
		if (self.mp == None):
			## create the reader object
			self.mp=FFMpegReader()

			## open an audio video file
			self.mp.open(self.currentFileSelectedFullPathName, TS_VIDEO_RGB24)
			self.tracks=self.mp.get_tracks()

			## connect audio to its device
			self.ap=AlsaSoundLazyPlayer(self.tracks[1].get_samplerate(),self.tracks[1].get_channels(),self.tracks[0].get_fps())
			self.tracks[1].set_observer(self.ap.push_nowait)
			self.tracks[0].set_observer(self.displayframe)
		self.mp.step()

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
