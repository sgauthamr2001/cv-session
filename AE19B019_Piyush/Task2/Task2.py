# -*- coding: utf-8 -*-
"""
Created on Sat Jul 10 23:35:28 2021

@author: PiyushBhujbal
"""

import cv2
#import numpy as np
import matplotlib.pyplot as plt

hurdle = cv2.imread("obstacle1.jpg")
hsv_hurdle = cv2.cvtColor(hurdle, cv2.COLOR_BGR2HSV)
hist = cv2.calcHist([hsv_hurdle],[0, 1], None, [180, 256], [0, 180, 0, 256])
norm = cv2.normalize(hist,hist, 0, 255, cv2.NORM_MINMAX)

disc = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (7,7))

video = cv2.VideoCapture("video.mp4")
while True:
    ret, frame = video.read()
    hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    
    
    
    res = cv2.calcBackProject([hsv_frame],[0,1],norm,[0,180,0,256],9)
    cv2.filter2D(res, -1, disc,res)
    
    #ret,thresh=cv2.threshold(res,5,255,cv2.THRESH_TOZERO)
    thresh = cv2.adaptiveThreshold(res,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY_INV,11,5)
    final=cv2.merge((thresh,thresh,thresh))
    result=cv2.bitwise_and(frame,final)
    
    cv2.imshow("result",result)
    
    if cv2.waitKey(1) == ord("q"):
        break
video.release()
cv2.destroyAllWindows()



plt.imshow(hist)
plt.show()
