# -*- coding: utf-8 -*-
"""
Created on Fri Jul  9 23:21:42 2021

@author: Varija
"""

import cv2 
import numpy as np
import matplotlib.pyplot as plt

# original_image = cv2.imread("full_image.jpg")
# hsv_original = cv2.cvtColor(original_image, cv2.COLOR_BGR2HSV)

#start the video
hurdle = cv2.imread("barrel.jpg")
# converting the barrel pic from RGB to HSV
hsv_hurdle = cv2.cvtColor(hurdle, cv2.COLOR_BGR2HSV)
#Histogram of Hurdle
hist_hurdle = cv2.calcHist([hsv_hurdle],[0,1], None, [180, 256], [0, 180, 0, 256])
# normalised histogram 
hist_norm = cv2.normalize(hist_hurdle,hist_hurdle,0, 255, cv2.NORM_MINMAX)
frame = cv2.VideoCapture("barrel.mp4")
disc = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (7,7))

while(frame.isOpened()):
    # Capture frame-by-frame
    ret, frames = frame.read()
    # Our operations on the frame come here
    hsv_video = cv2.cvtColor(frames, cv2.COLOR_BGR2HSV)
    rgb_video=cv2.cvtColor(frames, cv2.COLOR_BGR2RGB)
    h,s,v = cv2.split(hsv_video)
    
    res = cv2.calcBackProject([hsv_video],[0,1],hist_norm,[0,180,0,256],9)
      
    filt = cv2.filter2D(res, -1, disc, res)
    thresh=cv2.adaptiveThreshold(filt,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY_INV,11,5)
    
    # Overlay images using bitwise_and
    final = cv2.merge((thresh,thresh,thresh))
    
    result = cv2.bitwise_and(frames, final)
    # Display the resulting frame
    cv2.imshow('frame',filt)
    cv2.imshow('a',result) 
    if cv2.waitKey(1) == ord('q'):
        break

# When everything done, release the capture
frame.release()

cv2.destroyAllWindows()

plt.plot(hist_hurdle),plt.xlabel('Pixel intensity value'),plt.ylabel('Frequency'),plt.title('Histogram')

# cv2.imshow("original image", original_image)
# cv2.imshow("hurdle",hurdle)
# cv2.waitKey(0)
cv2.destroyAllWindows()

