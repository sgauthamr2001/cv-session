import cv2
img = cv2.imread(barrel.png,1)
img_hsv=cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
hsv_hist=cv2.calcHist([img_hsv],[0,1],None,[180,256],[0,180,0,256])
disc=cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(5,5))
vid=cv2.VideoCapture('video.mp4')
while vid.isOpened():
    bool, original=vid.read()
    if bool:
        original_hsv=cv2.cvtColor(original, cv2.COLOR_BGR2HSV)
        original_rgb=cv2.cvtColor(original, cv2.COLOR_BGR2RGB)
        mask=cv2.calcBackProject([original_hsv],[0,1],hsv_hist,[0,180,0,256],1)
        filtered=cv2.filter2D(mask,-1,disc)
        _,thresh=cv2.threshold(filtered,50,255,cv2.THRESH_BINARY)
        final=cv2.merge((thresh,thresh,thresh))
        result=cv2.bitwise_and(original_rgb,final)
        cv2.imshow('result',result)
    else:
        break
vid.release()
cv2.destroyAllWindows()