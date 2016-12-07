import numpy as np
import argparse
import cv2
from matplotlib import pyplot as plt

def pancake(imgurl, rad, tol, tol2, epsilon):
	# load image
	img = cv2.imread(imgurl)
	grayimg = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

	r = img.copy()
	g = img.copy()
	b = img.copy()
	whitebg = img.copy()

	#########################
	# Image levels
	#########################

	grayblur = cv2.bilateralFilter(grayimg, 100, 100, 0)

	# Lightest
	if (tol > 100): tol = 100
	if (tol < -100): tol = -100
	if (tol2 > 100): tol2 = 100
	if (tol2 < -100): tol2 = -100

	ret,thresh1 = cv2.threshold(grayblur, 193 + tol2, 255, cv2.THRESH_BINARY)
	# Middle
	ret,thresh2 = cv2.threshold(grayblur, 131 + tol2, 255, cv2.THRESH_BINARY)
	# Darkest
	ret,thresh3 = cv2.threshold(grayblur, 69 + tol, 255, cv2.THRESH_BINARY)

	# blue, lightest
	ret,canny1 = cv2.threshold(thresh1, 127, 255, cv2.THRESH_BINARY_INV)
	contours1,hierarchy1 = cv2.findContours(canny1, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

	approx3 = []
	for c in contours1:
		approx = cv2.approxPolyDP(c, epsilon, True)
		cv2.drawContours(b, [approx], -1, (255, 0, 0), -1)
		approx3.append(approx)


	# green, middle
	ret,canny2 = cv2.threshold(thresh2, 127, 255, cv2.THRESH_BINARY_INV)
	contours2,hierarchy2 = cv2.findContours(canny2, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

	approx2 = []
	for c in contours2:
		approx = cv2.approxPolyDP(c, epsilon, True)
		cv2.drawContours(g, [approx], -1, (0, 255, 0), -1)
		approx2.append(approx)

	# red, darkest
	ret,canny3 = cv2.threshold(thresh3, 127, 255, cv2.THRESH_BINARY_INV)
	contours3,hierarchy3 = cv2.findContours(canny3, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

	approx1 = []
	for c in contours3:
		approx = cv2.approxPolyDP(c, epsilon, True)
		cv2.drawContours(r, [approx], -1, (0, 0, 255), -1)
		approx1.append(approx)


	#########################
	# Perimeter
	#########################

	thresh = cv2.Canny(grayimg, 100, rad)
	contours,hierarchy = cv2.findContours(thresh, 1, 1)

	perimlines = []
	for c in contours:
		cv2.drawContours(img, [c], -1, (0, 0, 255), 2)
		perimlines.append(c)

	#########################
	# Outer image perimeter
	#########################

	# ret,whitethresh = cv2.threshold(grayblur, 200, 255, cv2.THRESH_BINARY_INV)
	# ret,cannyc = cv2.threshold(whitethresh, 127, 255, cv2.THRESH_BINARY_INV)
	# whitecontours,hierarchy4 = cv2.findContours(cannyc, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

	# for c in whitecontours:
	# 	approx = cv2.approxPolyDP(c, epsilon, True)
	# 	cv2.drawContours(whitebg, [approx], -1, (255, 0, 0), -1)

	# cv2.imshow("Brightest3", whitebg)





	cv2.imshow("Final", img)
	cv2.imshow("Brightest3", b)
	cv2.imshow("Brightest2", g)
	cv2.imshow("Brightest1", r)
	cv2.waitKey(0)

	return [perimlines, approx1, approx2, approx3]

# pancake('images/me.jpg', 101, 0, .35)
# pancake('images/id.jpg', 101, -60, -75, .35)
# pancake('images/smile.jpg', 101, 50, 40, 5)

























