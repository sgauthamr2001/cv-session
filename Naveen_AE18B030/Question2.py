import cv2


vid = cv2.VideoCapture("Barrel.mp4")

ref = cv2.imread("barrel.png")
hsv_ref = cv2.cvtColor(ref, cv2.COLOR_BGR2HSV)

ref_hist = cv2.calcHist([hsv_ref], [0, 1], None, [180, 256], [0, 180, 0, 256])
cv2.normalize(ref_hist,ref_hist,0,255,cv2.NORM_MINMAX)

while vid.isOpened():
    ret, original = vid.read()
    if not ret:
        print("Can't receive frame. Exiting ...")
        break
    hsv_original = cv2.cvtColor(original, cv2.COLOR_BGR2HSV)

    res = cv2.calcBackProject([hsv_original], [0, 1], ref_hist, [0, 180, 0, 256], 1)
    disc = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5, 5))
    res_1 = cv2.filter2D(res, -1, disc)
    _, thresh = cv2.threshold(res_1, 10, 255, cv2.THRESH_BINARY)

    final = cv2.merge((thresh, thresh, thresh))
    result = cv2.bitwise_and(original, final)

    cv2.imshow('RESULT', result)

    if cv2.waitKey(1) == ord('q'):
        break
vid.release()
cv2.destroyAllWindows()