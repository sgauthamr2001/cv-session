from os import system
system("cls")
import os
import cv2
from matplotlib import pyplot as plt
import numpy as np

path=os.path.dirname(os.getcwd())
os.chdir(path)
img=cv2.imread("media\einstein.jpg")
img1=cv2.GaussianBlur(img,(5,5),0.6)
img2=cv2.GaussianBlur(img,(9,9),5)

gauss_diff=cv2.absdiff(img1,img2)

plt.subplot(221),plt.imshow(img1),plt.title("gaussian blur-5x5 kernel"),plt.axis('off')
plt.subplot(222),plt.imshow(img2),plt.title("Gaussian blur-9x9 kernel"),plt.axis('off')
plt.subplot(223),plt.imshow(img),plt.title("Original"),plt.axis('off')
plt.subplot(224),plt.imshow(gauss_diff),plt.title("Edges Detected"),plt.axis('off')           #plotting original,filtered images,edges detected
plt.show()
cv2.waitKey(0)
