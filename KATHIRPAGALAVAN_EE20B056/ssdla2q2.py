import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

vin = cv.VideoCapture('barrelvid.mp4')
roi = cv.imread('barrelpic.png')
hsv = cv.cvtColor(roi,cv.COLOR_BGR2HSV)
roihist = cv.calcHist([hsv],[0, 1], None, [180, 256], [0, 180, 0, 256] )
cv.normalize(roihist,roihist,0,255,cv.NORM_MINMAX)
disc = cv.getStructuringElement(cv.MORPH_ELLIPSE,(5,5))


#frame_width = int(vin.get(3))
#frame_height = int(vin.get(4))
#out = cv.VideoWriter('EE20B056_barrelvid.avi',cv.VideoWriter_fourcc('M','J','P','G'), 10, (frame_width,frame_height))
while(vin.isOpened()):
    ret,frame=vin.read()
    hsvt = cv.cvtColor(frame,cv.COLOR_BGR2HSV)
    dst = cv.calcBackProject([hsvt],[0,1],roihist,[0,180,0,256],1)
    cv.filter2D(dst,-1,disc,dst)
    ret,thresh = cv.threshold(dst,150,255,0)
    thresh = cv.merge((thresh,thresh,thresh))
    res = cv.bitwise_and(frame,thresh)
    cv.imshow('result',res)
    #out.write(res)
    if cv.waitKey(25) & 0xFF == ord('q'):
        break
vin.release()