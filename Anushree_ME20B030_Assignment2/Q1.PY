import cv2
import numpy as np
from matplotlib import pyplot as plt
img=cv2.imread('einstein.png')
blur_g1=cv2.GaussianBlur(img,(5,5),0)
blur_g2=cv2.GaussianBlur(img,(9,9),1)
finalimg=blur_g1-blur_g2
plt.imshow(finalimg,cmap='gray'),plt.title("1st blur"),plt.axis("off")
plt.show()