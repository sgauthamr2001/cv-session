#########################################################
# Task1 : Edge Detection using Difference of Gaussians
#########################################################

import cv2

# Read the image from folder
img = cv2.imread('einstein.jpg')

# Find gaussian difference on image
img_5x5 = cv2.GaussianBlur(img,(5,5),1) 
img_9x9 = cv2.GaussianBlur(img,(9,9),10)
final = cv2.absdiff(img_5x5, img_9x9)

# Display result
cv2.imshow('Result', final)
cv2.waitKey()
