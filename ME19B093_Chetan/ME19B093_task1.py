import cv2
import matplotlib.pyplot as plt
import numpy as np

img = cv2.imread('einstein.jpg',0)

b1 = cv2.GaussianBlur(img,(5,5),1)
b2 = cv2.GaussianBlur(img,(9,9),100)

edges = b1-b2
plt.imshow(edges,cmap='gray')


