import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('einstein.jpg',1)
blur_gaus1 = cv2.GaussianBlur(img,(5,5),0)
blur_gaus2 = cv2.GaussianBlur(img,(9,9),5)

plt.imshow(img)
plt.figure(),plt.axis("off"),plt.title("Blurred Image 1"),plt.imshow(blur_gaus1)
plt.figure(),plt.axis("off"),plt.title("Blurred Image 2"),plt.imshow(blur_gaus2)
plt.show()

einstein1 = blur_gaus1 - blur_gaus2
einstein2 = -(blur_gaus1 - blur_gaus2)

plt.figure(),plt.axis("off"),plt.title("Detect Edge"),plt.imshow(einstein1)
plt.figure(),plt.axis("off"),plt.title("Detect Edge"),plt.imshow(einstein2)
plt.show()