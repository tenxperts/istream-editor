#!/usr/bin/python


#Anshuman : 22 June 2012 - Python library to manipulate video files

import sys
from av import *
from ctypes import *


def add_video_stream(oc, codec_id):
	st = av_new_stream(oc,0);
	if not st:
		print "Could not allocate video stream"
		return 0
	c = st.contents.codec
	c.contents.codec_id = codec_id
	c.codec_type = AVMEDIA_TYPE_VIDEO
	c.contents.bit_rate = 400000
	c.contents.width = 352
	c.contents.height = 288
	c.contents.time_base.den = 25
	c.contents.time_base.num = 1
	c.contents.gop_size = 12
	c.contents.pix_fmt = PIX_FMT_YUV420P
	
	return st

av_register_all()


#Anshuman : 22 June 2012 - Python module to merge two videos


#Pointers to av context for two videos
pFormatCtx1 = POINTER(AVFormatContext)()
pFormatCtx2 = POINTER(AVFormatContext)()

file1 = None
file2 = None

#Open the files
file1 = avformat_open_input(pFormatCtx1, sys.argv[1], None, None) 
if file1 == None:
	handle_error("could not open file ", sys.argv[1]) 

file2 = avformat_open_input(pFormatCtx2, sys.argv[2], None, None) 
if file2 == None:
	handle_error("could not open file", sys.argv[2]) 

if (av_find_stream_info(pFormatCtx1)<0):
	handle_error("could not read streams for ", sys.argv[1])

if (av_find_stream_info(pFormatCtx2)<0):
	handle_error("could not read streams for ", sys.argv[2])


#Acquire the video streams for the two files to be merged
videoStream1=-1;
i=0

for i in range(0,pFormatCtx1.contents.nb_streams):
    if(pFormatCtx1.contents.streams[i].contents.codec.contents.codec_type==AVMEDIA_TYPE_VIDEO):
        videoStream1=i;
        break;
if(videoStream1==-1):
    handle_error("Did not find a video stream ", sys.argv[1]) 


#Decode Step & Read Step

#Get a pointer to the codec context

pVideoCodecCtx1 = pFormatCtx1.contents.streams[videoStream1].contents.codec



#Get the video codec for file1 and file2

videoCodec1 = avcodec_find_decoder(pVideoCodecCtx1.contents.codec_id)

#open it

avcodec_open(pVideoCodecCtx1, videoCodec1);

print "opened codec "

if videoCodec1 == None:
	handle_error("Video Codec cannot be found for ", sys.argv[1])

print "Got video codecs for file 1"


#Read Video Packets & Audio packets from file 1

#Handle video for file1

pFrame1 = avcodec_alloc_frame()
LP_AVPicture = POINTER(AVPicture)
pFrameRGB1 = cast(pFrame1, LP_AVPicture)

print "Allocated an RGB Frame"

numBytes = avpicture_get_size(PIX_FMT_RGB24, pVideoCodecCtx1.contents.width, pVideoCodecCtx1.contents.height)

buffer = av_malloc(numBytes * sizeof(uint8_t))

LP_c_ubyte =  POINTER(c_ubyte)

bufferPtr = cast(buffer, LP_c_ubyte)
print "Allocated a buffer"

avpicture_fill(pFrameRGB1, bufferPtr, PIX_FMT_RGB24, pVideoCodecCtx1.contents.width, pVideoCodecCtx1.contents.height)
print "Filled a picture"


frameFinished1 = c_int(0)
pFrameFinished1 = pointer(frameFinished1)
packet1 =  AVPacket()
pPacket1 = pointer(packet1)
av_init_packet(pPacket1)
print pVideoCodecCtx1
print pFrame1
print pFrameFinished1
print pPacket1

#open a file for writing

fmt = av_guess_format(None, sys.argv[3], None)
print fmt.contents.name, " ", fmt.contents.mime_type, " ", fmt.contents.video_codec
oc=avformat_alloc_context()
oc.contents.oformat = fmt
oc.contents.filename=sys.argv[3]
print "flags ", oc.contents.oformat.contents.flags
video_st = add_video_stream(oc, fmt.contents.video_codec)

avio_open(oc.contents.pb, sys.argv[3], AVIO_FLAG_WRITE)
 


while(av_read_frame(pFormatCtx1, pPacket1)>=0): 
	if(packet1.stream_index==videoStream1): 
		av_write_frame(oc, pPacket1);
		print "written packet to output"
		'''
		# Decode video frame
    		avcodec_decode_video2(pVideoCodecCtx1, pFrame1, pFrameFinished1, pPacket1);
		# Did we get a video frame?
    		if not (frameFinished1 == c_int(0)):
			print "yeah got a decoded frame"
			pSWSContext = sws_getContext(pVideoCodecCtx1.contents.width, 
			pVideoCodecCtx1.contents.height, pVideoCodecCtx1.contents.pix_fmt, 
			pVideoCodecCtx1.contents.width, pVideoCodecCtx1.contents.height, PIX_FMT_RGB24,
                        SWS_BILINEAR, POINTER(SwsFilter)(), POINTER(SwsFilter)(), POINTER(c_double)());
                        sws_scale(pSWSContext, pFrame1.contents.data, pFrame1.contents.linesize, 0,
                        pVideoCodecCtx1.contents.height, pFrameRGB1.contents.data, 			
			pFrameRGB1.contents.linesize);
			print " yeah, scaled and converted the image to rgb "
                        av_free(pSWSContext);
		'''
		
    

	
    
  # Free the packet that was allocated by av_read_frame
av_free_packet(packet1);
