import cv2
import matplotlib.pyplot as plt
import numpy as np


kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5, 5))
kernel2 = np.ones((7, 7))
kernel3 = np.ones((5, 5))

roi = cv2.imread('../media/barrels/grass3.png')
hsv_roi =  cv2.cvtColor(roi, cv2.COLOR_BGR2HSV)
#cv2.imshow('roi',roi)
roi_hist = cv2.calcHist([hsv_roi], [0, 1], None, [100, 100], [0, 180, 0, 255])
#cv2.normalize(roi_hist, roi_hist, 0, 10, cv2.NORM_MINMAX)

vid = cv2.VideoCapture('../media/barrels/barrel.mp4')
while vid.isOpened():
    bool, original = vid.read()
    if bool:
        hsv_original = cv2.cvtColor(original, cv2.COLOR_BGR2HSV)
        cv2.imshow('original', original)

        mask = cv2.calcBackProject([hsv_original], [0, 1], roi_hist, [0, 180, 0, 256], 1)
        mask = cv2.filter2D(mask, -1, kernel)

        #mask = cv2.GaussianBlur(mask, (3, 3), 0)
        _, mask = cv2.threshold(mask, 10, 255, cv2.THRESH_BINARY)

        mask = cv2.dilate(mask, kernel, 2)
        #mask = cv2.erode(mask, kernel, 3)

        mask = cv2.bitwise_not(mask)

        cv2.imshow('mask', mask)

        mask = cv2.merge((mask, mask, mask))
        result = cv2.bitwise_and(original, mask)


        #cv2.imshow('mask',mask)
        cv2.imshow('result', result)

        if cv2.waitKey(10) & 0xFF == ord('q'):
            break
    else:
        break

vid.release()
cv2.destroyAllWindows()