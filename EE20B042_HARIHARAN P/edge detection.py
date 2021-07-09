import cv2
import numpy as np
from matplotlib import pyplot as plt

#Reading the image
img = cv2.imread('einstein.jpg')
blur_gaus1 = cv2.GaussianBlur(img,(5,5),0)
blur_gaus2 = cv2.GaussianBlur(img,(9,9),1.8)
result = cv2.subtract(blur_gaus1, blur_gaus2)
result1 = 255 - result
ret,thresh1 = cv2.threshold(result1,249,255,cv2.THRESH_BINARY)

#Plotting the images
plt.figure(),plt.axis("off"),plt.title("detected edges_neg"),plt.imshow(result1)
plt.subplot(231),plt.imshow(img,cmap='gray'),plt.title("Original Image"),plt.axis("off")
plt.subplot(232),plt.imshow(thresh1,cmap='gray'),plt.title("detected edge"),plt.axis("off")
plt.show()