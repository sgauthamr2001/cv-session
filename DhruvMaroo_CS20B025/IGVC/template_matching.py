#!/usr/bin/python3

import cv2

barrel_img = cv2.imread('roi.png') # get the image of the barrel
hsv_barrel = cv2.cvtColor(barrel_img, cv2.COLOR_BGR2HSV) # convert to hsv

barrel_hist = cv2.calcHist([hsv_barrel], [0, 2], None, [20, 256], [0, 20, 0, 256]) # calculate the histogram
cv2.normalize(barrel_hist, barrel_hist, 0, 255, cv2.NORM_MINMAX)# normalize the histogram

capture = cv2.VideoCapture('igvc.mp4') # create a capture using the video

valid = True

while valid: # loop as long as the frame is valid
	valid, frame = capture.read() # get the current frame

	hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV) # convert the frame to hsv

	back_proj = cv2.calcBackProject([hsv_frame], [0, 1], barrel_hist, [0, 20, 0, 256], 1) # calculate the backprojection (20, because orange lies in 0 to 20 hue)

	convol = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5, 5)) # generate the convolved disc element
	cv2.filter2D(back_proj, -1, convol, back_proj) # filter the back_proj using convol

	_1, thresh = cv2.threshold(back_proj, 70, 150, cv2.THRESH_BINARY) # apply threshold

	merged = cv2.merge((thresh, thresh, thresh)) # merge the thresholds

	final = cv2.bitwise_and(frame, merged) # apply bitwise and to get the common sections

	final = cv2.erode(final, (7, 7)) # erode to remove noise
	final = cv2.erode(final, (7, 7)) # erode again
	final = cv2.dilate(final, (5, 5)) # dilate to undo erosion
	final = cv2.GaussianBlur(final, (7, 7), 7) # apply gaussian blur to undo erosion and make the barrel blend in like a single object

	final = cv2.cvtColor(final, cv2.COLOR_BGR2GRAY) # convert this final image to gray

	conts = cv2.findContours(final.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[-2] # get the contours

	for c in conts: # for all the contours
		if cv2.contourArea(c) > 200: # if the area of the contour is significant
			(x, y, w, h) = cv2.boundingRect(c) # find the coordinates of a bounding rectangle
			cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2) # draw the bounding rectangle on frame

	cv2.imshow("IGVC Video", frame) # display the frame

	if cv2.waitKey(30) == 27: # wait till the user presses ESC
		break # break if ESC is pressed

cv2.destroyAllWindows() # destroy all windows
capture.release() # release the capture object