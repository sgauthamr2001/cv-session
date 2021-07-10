import cv2
import numpy as np
from matplotlib import pyplot as plt

#Reading the image
img = cv2.imread('barrels.jpg')
img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
img_hist = cv2.calcHist([img_hsv],[0, 1], None, [180, 256], [0, 180, 0, 255])
norm_hist_img = cv2.normalize(img_hist, img_hist, 0, 255, cv2.NORM_MINMAX)
cap = cv2.VideoCapture('videocvi.mp4')
if  (cap.isOpened()==False):
    print ("File Cannot be Opened")

frame_width = int(cap.get(3))
frame_height = int(cap.get(4))

out = cv2.VideoWriter('EE20B099.avi',cv2.VideoWriter_fourcc('M','J','P','G'), 10, (frame_width,frame_height))
while(cap.isOpened()):
    ret, frame = cap.read()
    if ret == True:
        hsv_frame=cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        res = cv2.calcBackProject([hsv_frame], [0, 1], norm_hist_img, [0, 180, 0, 255], 1)
        disc = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5,5))
        res=cv2.filter2D(res, -1, disc, res) 
        _, res =cv2.threshold(res,140,255,cv2.THRESH_BINARY)
        final=cv2.merge((res,res,res))
        result=cv2.bitwise_and(frame, final)
        cv2.imshow('result',result)
        out.write(result)
        if cv2.waitKey(10) & 0xFF == ord('q'):
            break
    else:
        print ("Frame is None")
        break

cap.release()
cv2.destroyAllWindows()
print 
"Video stop"




