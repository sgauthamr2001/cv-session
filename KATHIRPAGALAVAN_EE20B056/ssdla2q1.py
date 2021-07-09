import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('einstein.jpg',0)

gaussdiff=cv2.absdiff(cv2.GaussianBlur(img,(9,9),5),cv2.GaussianBlur(img,(5,5),2.15))

plt.subplot(121),plt.imshow(img,cmap='gray'),plt.title("Original Image"),plt.axis("off")
plt.subplot(122),plt.imshow(gaussdiff,cmap='gray'),plt.title("GaussDiffEdgeDetect"),plt.axis("off")
plt.show()