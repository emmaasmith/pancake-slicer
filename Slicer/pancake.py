import numpy as np
import argparse
import cv2
import math
from matplotlib import pyplot as plt

def pancake(imgurl, rad, tol, tol2, epsilon, white, imagetoggle, flip):

	#########################
	# Set up images
	#########################

	img = cv2.imread(imgurl)
	if flip:
		img = cv2.flip(img,1)
	grayimg = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

	r = img.copy()
	g = img.copy()
	b = img.copy()
	whitebg = img.copy()

	height, width, channels = img.shape
	
	#########################
	# Image levels
	#########################

	grayblur = cv2.bilateralFilter(grayimg, 100, 100, 0)

	# Tolerance caps
	if (tol > 100): tol = 100
	if (tol < -100): tol = -100
	if (tol2 > 100): tol2 = 100
	if (tol2 < -100): tol2 = -100

	# Lightest
	ret,thresh1 = cv2.threshold(grayblur, 193 + tol2, 255, cv2.THRESH_BINARY)
	# Middle
	ret,thresh2 = cv2.threshold(grayblur, 131 + tol2, 255, cv2.THRESH_BINARY)
	# Darkest
	ret,thresh3 = cv2.threshold(grayblur, 69 + tol, 255, cv2.THRESH_BINARY)

	# Lightest region
	ret,canny1 = cv2.threshold(thresh1, 127, 255, cv2.THRESH_BINARY_INV)
	contours1,hierarchy1 = cv2.findContours(canny1, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

	approx3 = []
	for c in contours1:
		approx = cv2.approxPolyDP(c, epsilon, True)
		cv2.drawContours(b, [approx], -1, (255, 0, 0), -1)
		approx3.append(approx)

	# Middle region
	ret,canny2 = cv2.threshold(thresh2, 127, 255, cv2.THRESH_BINARY_INV)
	contours2,hierarchy2 = cv2.findContours(canny2, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

	approx2 = []
	for c in contours2:
		approx = cv2.approxPolyDP(c, epsilon, True)
		cv2.drawContours(g, [approx], -1, (0, 255, 0), -1)
		approx2.append(approx)

	# Darkest region
	ret,canny3 = cv2.threshold(thresh3, 127, 255, cv2.THRESH_BINARY_INV)
	contours3,hierarchy3 = cv2.findContours(canny3, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

	approx1 = []
	for c in contours3:
		approx = cv2.approxPolyDP(c, epsilon, True)
		cv2.drawContours(r, [approx], -1, (0, 0, 255), -1)
		approx1.append(approx)


	#########################
	# Perimeter construction
	#########################

	thresh = cv2.Canny(grayblur, 150 - rad, 150 + rad)
	contours,hierarchy = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

	perimlines = []
	perimdoubled = []
	for c in contours:
		carea = cv2.contourArea(c)
		cperim = cv2.arcLength(c, True)
		# print carea, cperim, "   ", carea/(cperim)
		if cperim > 0.0:
			cx = cv2.approxPolyDP(c, epsilon, False)
			cv2.drawContours(img, [cx], -1, (0, 0, 255), 1)

			if (abs(carea/cperim) > 1):
				perimlines.append(cx)
			else:
				perimdoubled.append(cx)

	totperim = []
	for p in perimdoubled:
		phalf = len(p) / 2
		if phalf > 0:
			totperim.append(p[0:phalf+1])
	for p in perimlines:
		totperim.append(p)


	#########################
	# Outer image perimeter
	#########################

	WHITE = [255,0,0]
	whitethreshborder = cv2.copyMakeBorder(grayblur, 2, 2, 2, 2, cv2.BORDER_CONSTANT, value=WHITE)
	ret,whitethresh = cv2.threshold(whitethreshborder, 255 - white, 255, cv2.THRESH_BINARY_INV)
	whitecontours,hierarchy4 = cv2.findContours(whitethresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

	index = 0
	maxarea = 0
	maxindex = 0
	for c in whitecontours:
		warea = cv2.contourArea(c)
		if warea > maxarea:
			maxarea = warea
			maxindex = index
		index+=1

	approx = cv2.approxPolyDP(whitecontours[maxindex], epsilon, True)
	cv2.drawContours(whitebg, [approx], -1, (0, 0, 0), -1)


	#########################
	# Printing and return
	#########################

	if imagetoggle:
		cv2.imshow("Brightest3", b)
		cv2.imshow("Brightest2", g)
		cv2.imshow("Brightest1", r)
		cv2.imshow("Final", img)
		cv2.imshow("Outer", whitebg)
		cv2.waitKey(0)

	return [totperim, approx1, approx2, approx3, [approx]]
