import numpy as np
import cv2

disc = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (3,3))
barrel = cv2.imread('barrel.png', 1)
barrel_hsv = cv2.cvtColor(barrel, cv2.COLOR_BGR2HSV)

# Trial is the 
trial = cv2.imread('trial.png', 1)
trial_hsv = cv2.cvtColor(trial, cv2.COLOR_BGR2HSV)
barrel_hist = cv2.calcHist([barrel_hsv], [0], None, [180], [0, 180])

cap = cv2.VideoCapture('video.mp4')
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('output.avi', fourcc, 45 , (640, 360))

while cap.isOpened():
    ret, frame = cap.read()

    if ret==True:
        frame_hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

        mask = cv2.calcBackProject([frame_hsv], [0], barrel_hist, [0, 180], 1)
        mask = cv2.filter2D(mask, -1, disc)
        _, mask = cv2.threshold(mask, 150, 255, cv2.THRESH_BINARY)
        mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, np.ones((5,5)))
        final_mask = cv2.merge((mask, mask, mask))

        result = cv2.bitwise_and(frame, final_mask)
        
        out.write(result)
        cv2.imshow('Mask', result)
        cv2.imshow('Original video', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    else:
        break

cap.release()
out.release()
cv2.destroyAllWindows()