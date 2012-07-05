#!/usr/bin/python

import sys
from PIL import Image
from sys import stdout
from scipy import fftpack
import math
import numpy



def scale(im,size):
	im = im.resize((size, size), Image.ANTIALIAS)
	return im

def gray_scale(im):
	im = im.convert('L')
	return im

def print_pixels(im):
	pixels = im.load()
	width, height = im.size
	for x in range(width):
		for y in range(height):
			print pixels[x,y]

def getBlue(im):
	pixels = im.load()
	width, height = im.size
	for x in range(width):
		for y in range(height):
			pixel =  pixels[x,y]
			blue = pixel & 0xff
			im.putpixel((x,y), blue)
	return im

def initCoefficients(size):
	c = numpy.empty((size))
	for i in range(size):
		c[i] = 1
	c[0] = 1/math.sqrt(2)
	return c


def apply_dct(f, size, c):
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


def compute_hash_from_dct_vals(dctVals, size, smallerSize):
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

def to_decimal(x):
    return sum(map(lambda z: int(x[z]) and 2**(len(x) - z - 1),
                   range(len(x)-1, -1, -1)))


def compute_dct_hash(im):
	im = scale(im, 32)
	im = gray_scale(im)
	im = getBlue(im)
	c = initCoefficients(32)
	dctVals = apply_dct(im, 32, c)
	hash = compute_hash_from_dct_vals(dctVals, 32, 8)
	hash = to_decimal(hash)
	return hash
	
	
im = Image.open(sys.argv[1])
print compute_dct_hash(im)

