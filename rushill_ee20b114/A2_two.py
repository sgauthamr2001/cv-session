import cv2
import numpy as np

fourcc = cv2.VideoWriter_fourcc(*'mp4v')
iter=cv2.VideoWriter('final.mp4', fourcc, 30, (854,480))

video_stream = cv2.VideoCapture('video.mp4')

tframes = video_stream.get(cv2.CAP_PROP_FRAME_COUNT)

roi = cv2.imread('roi.png')

hsv = cv2.cvtColor(roi,cv2.COLOR_BGR2HSV)
roihist = cv2.calcHist([hsv],[0, 1], None, [100, 100], [0, 180, 0, 256] )
cv2.normalize(roihist,roihist,0,255,cv2.NORM_MINMAX)

for i in range(int(tframes)):
 

    _, frame = video_stream.read()
    hsv = cv2.cvtColor(frame, cv2.COLOR_RGB2HSV)
    res = cv2.calcBackProject([hsv], [0, 1], roihist, [0, 180, 0, 256], 1)
    disc = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5,5))
    cv2.filter2D(res, -1, disc, res)
    _, thresh = cv2.threshold(res, 20, 255, cv2.THRESH_BINARY)
    final = cv2.merge((thresh,thresh,thresh))
    result = cv2.bitwise_and(frame, final)
    kernel = np.ones((3, 3), np.uint8)
    result = cv2.dilate(result, kernel, iterations = 1)


    iter.write(frame)
   
iter.release()


    



