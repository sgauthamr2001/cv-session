import cv2
import numpy as np
from matplotlib import pyplot as plt
img=cv2.imread('einstein.jpg',0)
gaus_blur5=cv2.GaussianBlur(img,(5,5),0.5)
gaus_blur9=cv2.GaussianBlur(img,(9,9),5)
edges=cv2.subtract(gaus_blur5,gaus_blur9)
cv2.imshow('edge_detection',edges)
cv2.waitKey(0)
