# -*- coding: utf-8 -*-
"""cv_session.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1hoI-_-6hb8gBxU2aS9WxQmz0wjQrJ4fb
"""

# Commented out IPython magic to ensure Python compatibility.
! git clone https://github.com/nbala2k2/cv-session
# %cd cv-session/

"""# Question-1"""

import matplotlib
import matplotlib.pyplot as plt
import cv2
from google.colab.patches import cv2_imshow
import numpy as np

img='media/einstein.jpg'
img=cv2.imread(img)
blur_gaus1 = cv2.GaussianBlur(img,(5,5),1)
blur_gaus2=  cv2.GaussianBlur(img,(9,9),30)
result=blur_gaus1-blur_gaus2

plt.figure(),plt.axis("off"),plt.title("Original Image"),plt.imshow(img)
plt.figure(),plt.axis("off"),plt.title("Blurred Image"),plt.imshow(result)
plt.show()

"""# Question 2:-"""

import cv2
from matplotlib import pyplot as plt
from google.colab.patches import cv2_imshow
import numpy as np
capture = cv2.VideoCapture('media/video.mp4')
img = cv2.imread("media/barrel1.JPG")
img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
plt.imshow(img_hsv)
# histogram
img_hist = cv2.calcHist([img_hsv], [0, 2], None, [180, 256], [0, 180, 0, 256])
ret = True
while ret == True :
    ret, frame = capture.read()
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    res = cv2.calcBackProject([hsv], [0, 2], img_hist, [0, 180, 0, 256], scale=1)
    disc = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5,5))
    cv2.filter2D(res, -1, disc, res)
    _, thresh = cv2.threshold(res, 20, 255, cv2.THRESH_BINARY)
    final = cv2.merge((thresh,thresh,thresh))
    result = cv2.bitwise_or(frame, final)
    cv2_imshow(result)
    ret, frame = capture.read()

capture.release()
print("FINISHED")