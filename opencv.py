import cv2
import numpy as np


framewidth = 640
frameheight = 480
cap = cv2.VideoCapture(0)
cap.set(3, framewidth)
cap.set(4, frameheight)
cap.set(10, 150)


colors = [[0,117,124,179,255,255]]                        ##[hmin,smin,vmin,hmax,smax,vmax]   ## Blue
colorVAL = [[182,173,50]]                                 ##BGR
mypoints = []                                             ##[x, y, colorid]


def findColor(img,colors,colorVAL):
    count = 0
    newpts = []
    
    HSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    
    for color in colors:
        lower = np.array(color[0:3])
        upper = np.array(color[3:6])
        mask = cv2.inRange(HSV,lower,upper)
        x,y=getContours(mask)
        cv2.circle(Res, (x,y), 10, colorVAL[count], cv2.FILLED)
        
        if x!=0 and y!=0:
            newpts.append([x,y,count])
        count+=1
        cv2.imshow(str(color[0]),mask)
        
    return newpts    


def getContours(img):
    
    contours, hierarchy = cv2.findContours(img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    x,y,w,h = 0,0,0,0
    
    for cnt in contours:
       area = cv2.contourArea(cnt)
    
       if area>500:
           #cv2.drawContours(Res, cnt, -1, (255,0,0), 3)
           perimeter = cv2.arcLength(cnt, True)
           approx = cv2.approxPolyDP(cnt, 0.02*perimeter, True)
           x,y,w,h = cv2.boundingRect(approx) 
            
    return x+w//2,y     


def drawoncanvas(mypoints, colorVAL):
   for point in mypoints:
       cv2.circle(Res, (point[0],point[1]), 10, colorVAL[point[2]], cv2.FILLED)

        
while True:
    success, img = cap.read()
    Res = img.copy()
    newpts = findColor(img,colors,colorVAL)
    
    if len(newpts)!=0:
        for newpt in newpts:
            mypoints.append(newpt)
            
    if len(mypoints)!=0:
        drawoncanvas(mypoints,colorVAL)        
    cv2.imshow("Result",Res)
    
    if cv2.waitKey(1) & 0xFF==ord('q'):
        break
