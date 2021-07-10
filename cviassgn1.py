import cv2
import numpy as np
from matplotlib import pyplot as plt
img=cv2.imread('../einstein.png')
blur_gaus5 = cv2.GaussianBlur(img,(5,5),40)
blur_gaus9 = cv2.GaussianBlur(img,(9,9),5)
plt.figure(),plt.axis("off"),plt.title("Original Image"),plt.imshow(img)
plt.figure(),plt.axis("off"),plt.title("Blurred Image5"),plt.imshow(blur_gaus5)
plt.figure(),plt.axis("off"),plt.title("Blurred Image9"),plt.imshow(blur_gaus9)
plt.figure(),plt.axis("off"),plt.title("9-5"),plt.imshow(blur_gaus9-blur_gaus5)
plt.show()