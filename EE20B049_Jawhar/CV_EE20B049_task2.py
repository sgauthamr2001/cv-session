import cv2
import numpy as np
#from matplotlib import pyplot as plt

barrel = cv2.imread(r'C:\Users\Jawhar\Downloads\ROI_Barrel.png')
hsv_barrel = cv2.cvtColor(barrel,cv2.COLOR_BGR2HSV)
orig_vid = cv2.VideoCapture(r'C:\Users\Jawhar\Videos\CV_Video.mp4')
# calculating object histogram
hist_roi = cv2.calcHist([hsv_barrel], [0, 1], None, [180, 256], [0, 180, 0, 256])
# normalize histogram
cv2.normalize(hist_roi, hist_roi, 0, 255, cv2.NORM_MINMAX)
disc = cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(5,5))

while(orig_vid.isOpened()):
    ret,frame=orig_vid.read()
    hsv_frame = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    res = cv2.calcBackProject([hsv_frame],[0,1],hist_roi,[0,180,0,256],1)
    cv2.filter2D(res, -1, disc, res)
    # Use thresholding to segment out the region
    ret, thresh = cv2.threshold(res, 100, 255, 0)

    # Overlay images using bitwise_and
    final = cv2.merge((thresh, thresh, thresh))
    result = cv2.bitwise_and(frame, final)
    cv2.imshow('Computer sees barrels!', result)
    if cv2.waitKey(30) == 27:
        break

cv2.destroyAllWindows()
orig_vid.release()
