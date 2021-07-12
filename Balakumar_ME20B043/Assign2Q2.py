import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt


roi = cv.imread("orange_whiteobj.png")
hsv = cv.cvtColor(roi, cv.COLOR_BGR2HSV)

orange = np.uint8([[[0, 69, 255]]])
hsv_orange = cv.cvtColor(orange,cv.COLOR_BGR2HSV) # 8 ,255,255

cap = cv.VideoCapture("video.mp4")

while True:
    ret, original_image = cap.read()
    hsvt = cv.cvtColor(original_image, cv.COLOR_BGR2HSV)
        # calculating object histogram
    roihist = cv.calcHist([hsv],[0, 1], None, [180, 256], [0, int(hsv_orange[0,0,0]) , 0, int(hsv_orange[0,0,1]) ] )
        # normalize histogram and apply backprojection
    cv.normalize(roihist,roihist,0,255,cv.NORM_MINMAX)
    res = cv.calcBackProject([hsvt],[0,1],roihist,[0,int(hsv_orange[0,0,0]),0,int(hsv_orange[0,0,1]) ],1)
        # Now convolute with circular disc
    disc = cv.getStructuringElement(cv.MORPH_ELLIPSE,(5,5))
    cv.filter2D(res,-1,disc,res)
    # threshold and binary AND

    ret,thresh = cv.threshold(res,120,250,cv.THRESH_BINARY)
    final = cv.merge((thresh,thresh,thresh))
    res = cv.bitwise_and(original_image,final)
    # cv.imshow("obj_detect",res)          # To view the barrel in bitwise and
    


    contours, _ = cv.findContours(thresh, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
    
    for c in contours:
        rect = cv.boundingRect(c)
        x,y,w,h = rect
        if cv.contourArea(c)>500 :
            cv.rectangle(original_image,(x,y),(x+w,y+h),(255,255,255),2)

    # Displaying original image with boxes around the obstacle 
   
    cv.imshow("obj_detect",original_image)
    #Press q to exit
    if cv.waitKey(1) == ord('q'):
        break

cap.release()
cv.destroyAllWindows()











