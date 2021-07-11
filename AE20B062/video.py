import cv2
import matplotlib.pyplot as plt
import numpy as np

vid = cv2.VideoCapture("./vid.mp4")

roi = cv2.imread("./barrel.png")
roi_hsv = cv2.cvtColor(roi, cv2.COLOR_BGR2HSV)
roi_hist = cv2.calcHist([roi_hsv], [0], None, [180], [0, 180])
roi_norm = cv2.normalize(roi_hist, 0, 255, cv2.NORM_MINMAX)

disc = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5, 5))

while vid.isOpened():
    ret, frame = vid.read()
    if ret:
        frame_hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        res = cv2.calcBackProject([frame_hsv], [0, 1], roi_norm, [0, 180, 0, 256], 1)
        cv2.filter2D(res, -1, disc, res)
        cv2.normalize(res, res, 0, 255, cv2.NORM_MINMAX)
        ret_, thresh = cv2.threshold(res, 50, 255, cv2.THRESH_BINARY)
        final = cv2.merge((thresh, thresh, thresh))
        result = cv2.bitwise_and(frame, final)

        cv2.imshow("", result)
        if cv2.waitKey(25) & 0xFF == ord('q'):
            break

    else:
        break
