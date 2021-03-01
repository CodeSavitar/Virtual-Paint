import cv2
import numpy as np

def empty(a):
    pass

cap = cv2.VideoCapture(0)
cap.set(3, 320)
cap.set(4, 240)
cap.set(10, 150)

cv2.namedWindow("Trackbars")
cv2.resizeWindow("Trackbars",320,240)
cv2.createTrackbar("Hue min","Trackbars",0,179,empty)
cv2.createTrackbar("Hue max","Trackbars",179,179,empty)
cv2.createTrackbar("Sat min","Trackbars",0,255,empty)
cv2.createTrackbar("Sat max","Trackbars",255,255,empty)
cv2.createTrackbar("Val min","Trackbars",0,255,empty)
cv2.createTrackbar("Val max","Trackbars",255,255,empty)

while True:
    _, img = cap.read()
    HSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    h_min=cv2.getTrackbarPos("Hue min","Trackbars")
    h_max=cv2.getTrackbarPos("Hue max","Trackbars")
    s_min=cv2.getTrackbarPos("Sat min","Trackbars")
    s_max=cv2.getTrackbarPos("Sat max","Trackbars")
    v_min=cv2.getTrackbarPos("Val min","Trackbars")
    v_max=cv2.getTrackbarPos("Val max","Trackbars")
    print(h_min)

    lower = np.array([h_min,s_min,v_min])
    upper = np.array([h_max,s_max,v_max])
    mask = cv2.inRange(HSV, lower, upper)
    result = cv2.bitwise_and(img,img,mask=mask)

    mask = cv2.cvtColor(mask, cv2.COLOR_GRAY2BGR)
    hStack = np.hstack([img, mask, result])
    cv2.imshow('Hoizontal stack',hStack)
    if cv2.waitKey(1) and 0xFF==ord('q'):
        break
