import cv2
import numpy

img = cv2.imread(r"C:\Users\MelPr\PycharmProjects\pythonProject1\einstein.jpg", 0)
blur_gaus_9 = cv2.GaussianBlur(img,(9,9),0)
blur_gaus_5 = cv2.GaussianBlur(img,(5,5),0)

NewEinstein = blur_gaus_9 - blur_gaus_5
cv2.imshow('Einstein Edges', NewEinstein)
cv2.waitKey(0)
