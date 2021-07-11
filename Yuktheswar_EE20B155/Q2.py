from os import system
system("cls")
import cv2

video=cv2.VideoCapture("barrelvideo.mp4")                                # reads video from disk

Region = cv2.imread('pathnew.png')                                         # template for lines bounding the path
HSV_ver = cv2.cvtColor(Region,cv2.COLOR_BGR2HSV)                           
hist=cv2.calcHist([HSV_ver],[1,0],None,[256,256],[0,256,0,256])            # Histogram of HSV distribution of  template
cv2.normalize(hist,hist,0,255,cv2.NORM_MINMAX) 
       
Region1 = cv2.imread('barrelnew.png')                                      # template for the barrels    
HSV_ver1 = cv2.cvtColor(Region1,cv2.COLOR_BGR2HSV)                         
hist1=cv2.calcHist([HSV_ver1],[1,0],None,[256,256],[0,256,0,256])          # Histogram of HSV distribution of  template
cv2.normalize(hist1,hist1,0,255,cv2.NORM_MINMAX)

disc = cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(5,5))                  #kernel to convolve

while(video.isOpened()):
     
    ret,frame=video.read()                                                 # a frame in the video
    hsvf= cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)                            # HSV distribution of the frame

    prj= cv2.calcBackProject([hsvf],[1,0],hist,[0,256,0,256],1)            # Trying to locate the templates in the frame
    prj1= cv2.calcBackProject([hsvf],[1,0],hist1,[0,256,0,256],1)


    cv2.filter2D(prj,-1,disc,prj)                                           # Convolution and thresholding 
    ret,thresh=cv2.threshold(prj,150,255,0)
    thresh = cv2.merge((thresh,thresh,thresh))

    cv2.filter2D(prj1,-1,disc,prj1)                                         # Convolution and thresholding
    ret,thresh1=cv2.threshold(prj1,180,255,0)
    thresh1 = cv2.merge((thresh1,thresh1,thresh1))

    result = cv2.bitwise_or(thresh1,thresh)                                 # Bitwise or is used to get  both barrels and lines in the same array
    result = cv2.bitwise_and(frame,result)

    cv2.imshow('result',result)
    cv2.imshow('original',frame)
    if cv2.waitKey(1) & 0xFF == ord('e'):
        break
video.release()
