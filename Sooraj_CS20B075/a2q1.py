#!/usr/bin/env python3
import cv2

img = cv2.imread('einstein.jpg', 0)

# make two images with kernels of different sizes

gblur1 = cv2.GaussianBlur(img, (5, 5), 0.1)
gblur2 = cv2.GaussianBlur(img, (9, 9), 5)

# find the difference between the images to get a rough edge detection

edge_detect = cv2.absdiff(gblur1, gblur2)
cv2.imwrite('edgy_einstein.jpg', edge_detect)


