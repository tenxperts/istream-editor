LIBAVFORMATPATH = -L/home/anshu/Documents/Applications/FFMpeg/ffmpeg/ffmpeg/libavformat
LIBAVCODECPATH = -L/home/anshu/Documents/Applications/FFMpeg/ffmpeg/ffmpeg/libavcodec
LIBAVUTILPATH = -L/home/anshu/Documents/Applications/FFMpeg/ffmpeg/ffmpeg/libavutil
LIBSWSCALEPATH = -L/home/anshu/Documents/Applications/FFMpeg/ffmpeg/ffmpeg/libswscale
LIBAVINCPATH = -I/home/anshu/Documents/Applications/FFMpeg/ffmpeg/ffmpeg/

all: avcodecsample VideoEditor

avcodecsample: avcodec_sample.cpp
	g++ -w $(LIBAVINCPATH) $(LIBAVCODECPATH) $(LIBAVUTILPATH) $(LIBSWSCALEPATH)  $(LIBAVFORMATPATH) avcodec_sample.cpp -o avcodecsample  -lavformat -lavcodec -lavutil -lswscale -lz -lm
	
VideoEditor:
	g++ VideoEditor.cpp -o VideoEditor `pkg-config --cflags --libs libglade-2.0 gtk+-2.0`
