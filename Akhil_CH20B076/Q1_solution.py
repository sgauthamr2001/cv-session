"""
CV-Session-1 Assignment
Question-1 Solution

By: P Akhil Reddy
Roll No: CH20B076
Contact: 8074147570
Email: ch20b076@smail.iitm.ac.in

Problem Statement: Edge Detection of an image using Difference of Gaussians
"""
import cv2

img = cv2.imread('einstein.jpg')
#reads the einstein image

blur_gaus1 = cv2.GaussianBlur(img, (9, 9), 0)
blur_gaus2 = cv2.GaussianBlur(img, (5, 5), 0)
#blurs the image using two different gaussian filters

img2 = blur_gaus2 - blur_gaus1
#finds the difference between the two blurred images, which is nothing but the edges of einstein image

#finally display the image of edges
cv2.imshow('Einstein Edges', img2)
cv2.waitKey()