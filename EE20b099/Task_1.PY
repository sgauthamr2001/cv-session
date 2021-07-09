import cv2
import numpy as np
from matplotlib import pyplot as plt

#Reading the image
img = cv2.imread('einstein.jpg')
b1 = cv2.GaussianBlur(img,(5,5),0)
b2 = cv2.GaussianBlur(img,(9,9),1.5)
final=(b2-b1)
ret,thresh= cv2.threshold(final,239,255,cv2.THRESH_BINARY)

#Plotting the images
plt.subplot(121),plt.imshow(thresh,cmap='gray'),plt.title("edge finding"),plt.axis("off")
plt.subplot(122),plt.imshow(img,cmap='gray'),plt.title("original"),plt.axis("off")
plt.show()