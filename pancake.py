import numpy as np
import argparse
import cv2


def pancake(inF, offset):
	# load image
	img = cv2.imread(args["image"])
	grayimg = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
	# blue = img.copy()
	# green = img.copy()
	# red = img.copy()

	#########################
	# Image levels
	#########################

	grayblur = cv2.bilateralFilter(grayimg, args["radius"], args["radius"], 0)

	epsilon = 0.00001 * args["tolerance"]

	# Lightest
	ret,thresh1 = cv2.threshold(grayblur, 193, 255, cv2.THRESH_BINARY)
	# Middle
	ret,thresh2 = cv2.threshold(grayblur, 131, 255, cv2.THRESH_BINARY)
	# Darkest
	ret,thresh3 = cv2.threshold(grayblur, 69, 255, cv2.THRESH_BINARY)

	# cv2.imshow("Brightest2", thresh2)
	# cv2.imshow("Brightest3", thresh3)


	# blue, lightest
	ret,canny1 = cv2.threshold(thresh1,127,255,cv2.THRESH_BINARY_INV)
	contours1,hierarchy1 = cv2.findContours(canny1, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

	for c in contours1:
		approx = cv2.approxPolyDP(c, epsilon, True)
		cv2.drawContours(img, [approx], -1, (255, 0, 0), -1)
		print approx


	# green, middle
	ret,canny2 = cv2.threshold(thresh2,127,255,cv2.THRESH_BINARY_INV)
	contours2,hierarchy2 = cv2.findContours(canny2, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

	for c in contours2:
		approx = cv2.approxPolyDP(c, epsilon, True)
		cv2.drawContours(img, [approx], -1, (0, 255, 0), -1)


	# red, darkest
	ret,canny3 = cv2.threshold(thresh3,127,255,cv2.THRESH_BINARY_INV)
	contours3,hierarchy3 = cv2.findContours(canny3, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

	for c in contours3:
		approx = cv2.approxPolyDP(c, epsilon, True)
		cv2.drawContours(img, [approx], -1, (0, 0, 255), -1)



	#########################
	# Perimeter
	#########################

	thresh = cv2.Canny(grayimg, 100, 100+args["tolerance"])
	contours,hierarchy = cv2.findContours(thresh, 1, 1)

	for c in contours:
		cv2.drawContours(img, [c], -1, (255, 255, 255), 2)


	cv2.imshow("Brightest3", thresh3)

	cv2.imshow("Final", img)
	cv2.waitKey(0)






























