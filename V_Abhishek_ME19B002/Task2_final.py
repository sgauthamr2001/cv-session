import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('barrel1.png',1)
img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
hsv_hist = cv2.calcHist([img_hsv],[0,1],None,[180,256],[0,180,0,256])
disc = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5,5))
vid = cv2.VideoCapture('video.mp4')
while vid.isOpened():
    bool, original = vid.read()
    if bool:
        original_hsv = cv2.cvtColor(original, cv2.COLOR_BGR2HSV)
        mask = cv2.calcBackProject([original_hsv],[0,1],hsv_hist,[0,180,0,256],1)
        filtered = cv2.filter2D(mask, -1, disc)
        _,thresh = cv2.threshold(filtered, 50, 255, cv2.THRESH_BINARY)
        final = cv2.merge((thresh,thresh,thresh))
        result = cv2.bitwise_and(original, final)
        cv2.imshow("result",result)
        if cv2.waitKey(25) & 0xFF == ord('q'):
            break
    else:
        break
vid.release()
cv2.destroyAllWindows()