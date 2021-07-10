import cv2

def get_roi_hist(roi):
    roi_hsv = cv2.cvtColor(roi, cv2.COLOR_BGR2HSV)
    roi_hist = cv2.calcHist([roi_hsv],[0], None, [180], [0, 180])
    return roi_hist

def get_mask(img,roi_hist,morph=0):
    img_hsv = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
    mask = cv2.calcBackProject([img_hsv],[0],roi_hist,[0,180],1)
    if morph:
        disc = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5, 5))
        mask = cv2.filter2D(mask,-1,disc)
    _,mask = cv2.threshold(mask,120,255,cv2.THRESH_BINARY)
    return mask

cap = cv2.VideoCapture('Video.mp4')
barrel = cv2.imread('ROI.png')

roi_hist = get_roi_hist(barrel)
frame_size = (720,1280)

while(cap.isOpened()):
    ret, frame = cap.read()
    
    if ret == True:
        cv2.imshow('Frame',frame)
        mask = get_mask(frame,roi_hist)
        cv2.imshow('Mask',mask)
        final = cv2.bitwise_and(frame,frame,mask=mask)
        cv2.imshow('Only Barrels!',final)

        if cv2.waitKey(25) & 0xFF == ord('q'):
            break
    else: 
        break

cap.release()
cv2.destroyAllWindows()
out.release()


