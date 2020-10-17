import numpy as np
import cv2
import time

cap = cv2.VideoCapture(0)
time.sleep(3)
fgbg = cv2.createBackgroundSubtractorMOG2(history=0, varThreshold=50)

while(cap.isOpened()):
    ret, frame = cap.read()
    if frame is not None:
        frame = fgbg.apply(frame)
        cv2.imshow('frame', frame)
        # frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        # frame = cv2.flip(frame, -1)
        frame = cv2.GaussianBlur(frame, (41, 41), 0)
        # ret, frame = cv2.threshold(frame, 5, 255, cv2.THRESH_BINARY)
        # frame = cv2.adaptiveThreshold(
        #     frame, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2)
        frame = cv2.Canny(frame, 50, 100)
        cv2.imshow('frame', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break
cap.release()
cv2.destroyAllWindows()
