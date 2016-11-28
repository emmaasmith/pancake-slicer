import numpy as np
import argparse
import cv2

# parsing
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", help = "img file")
ap.add_argument("-r", "--radius", type = int, help = "blur radius, odd #")
ap.add_argument("-t", "--tolerance", type = int, help = "tolerance 1-300")
args = vars(ap.parse_args())

# load image
img = cv2.imread(args["image"])
grayimg = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# apply a Gaussian blur to the image
# grayblur = cv2.bilateralFilter(grayimg, args["radius"], args["radius"], 0)
# (minVal, maxVal, minLoc, maxLoc) = cv2.minMaxLoc(grayblur)
# find brightest area
# cv2.circle(image, maxLoc, args["tolerance"], (255, 0, 0), 2)
# display the results of our newly improved method
# cv2.imshow("Brightest area", grayblur)
# cv2.waitKey(0)


#########################
# Perimeter
#########################

thresh = cv2.Canny(grayimg, 100, 100+args["tolerance"])
contours,hierarchy = cv2.findContours(thresh, 1, 2)

# for c in contours:
# 	cv2.drawContours(img, [c], -1, (0, 255, 0), 5)

# cv2.imshow("Brightest area", img)
# cv2.waitKey(0)



#########################
# Image levels
#########################






############### THIS IS THE KEYPOINT APPROACH

grayblur = cv2.bilateralFilter(grayimg, args["radius"], args["radius"], 0)

# # Setup SimpleBlobDetector parameters.
# params = cv2.SimpleBlobDetector_Params()
 
# # Change thresholds
# params.minThreshold = 10;
# params.maxThreshold = 200;
 
# # Filter by Area.
# params.filterByArea = True
# params.minArea = 5
 
# # Filter by Circularity
# params.filterByCircularity = False
 
# # Filter by Convexity
# params.filterByConvexity = True
# params.minConvexity = 0.87
 
# # Filter by Inertia
# params.filterByInertia = True
# params.minInertiaRatio = 0.01
 
# # Create a detector with the parameters
# ver = (cv2.__version__).split('.')
# if int(ver[0]) < 3 :
#     detector = cv2.SimpleBlobDetector(params)
# else : 
#     detector = cv2.SimpleBlobDetector_create(params)


# # Detect blobs.
# keypoints = detector.detect(grayblur)
 
# # Draw detected blobs as red circles.
# imgblobs = cv2.drawKeypoints(grayblur, keypoints, np.array([]), (0,0,255), cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)

# # Show keypoints
# cv2.imshow("Keypoints", imgblobs)
# cv2.waitKey(0)






############### THIS IS THE CONTOUR APPROACH

# cnt = contours[0]


# for c in contours:
# 	perimeter = cv2.arcLength(c, True)
# 	epsilon = perimeter * 0.01
# 	approx = cv2.approxPolyDP(c, epsilon, True)
	 
# 	for a in approx:
# 		cv2.drawContours(img, [a], -1, (0, 255, 0), 5)

# cv2.imshow("Brightest area", img)
# cv2.waitKey(0)





############### THIS IS THE THRESHOLD APPROACH
# 3 is given when pixel is more than 2

# Lightest
ret,thresh1 = cv2.threshold(grayblur, 193, 255, cv2.THRESH_BINARY)
# Middle
ret,thresh2 = cv2.threshold(grayblur, 131, 255, cv2.THRESH_BINARY)
# Darkest
ret,thresh3 = cv2.threshold(grayblur, 69, 255, cv2.THRESH_BINARY)


cv2.imshow("Brightest1", thresh1)
cv2.imshow("Brightest2", thresh2)
cv2.imshow("Brightest3", thresh3)
cv2.waitKey(0)






























