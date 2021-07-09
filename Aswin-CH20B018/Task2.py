###########################################
# Task 2: Template Matching using Histograms
###########################################

import cv2

# Create histogram of target and normalize
raw_target = cv2.imread('Barrel.jpg')
target_hsv = cv2.cvtColor(raw_target, cv2.COLOR_BGR2HSV)
target_hist = cv2.calcHist([target_hsv],[0,1], None, [180,256], [0,180,0,256])
cv2.normalize(target_hist, target_hist, 0, 255, cv2.NORM_MINMAX)
print(target_hsv.shape)

# Defining kernel matrix for 2D filter
disc = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5,5))

# Find target in every frame of video
video = cv2.VideoCapture('Full_video.mp4')
if video.isOpened():
    rval,frame = video.read()
    while rval:
        hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        res = cv2.calcBackProject([hsv_frame], [0,1], target_hist, [0, 180, 0, 256], scale=1)
        cv2.filter2D(res, -1, disc, res)
        ret,thresh = cv2.threshold(res,thresh=60,maxval=255,type=cv2.THRESH_BINARY)
        final = cv2.merge((thresh,thresh,thresh))
        result = cv2.bitwise_or(frame, final)
        
        # Display result
        cv2.imshow('Final result (Press \'x\' to exit)', result)
        # Wait for input and proceed
        if cv2.waitKey(1) == ord('x'):
            break
        # Read next frame
        rval,frame=video.read()

# Free-up memory
video.release()
