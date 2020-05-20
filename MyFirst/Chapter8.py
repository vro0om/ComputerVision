import cv2
import StackImage as si
import numpy as np

def getContours(img):
    contours,hierarchy = cv2.findContours(img,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
    for cnt in contours:
        area = cv2.contourArea(cnt)
        print(area)
        if area>500:
            cv2.drawContours(imgContour,cnt,-1,(255,0,0),3)

            #Perimeter Detection
            perimeter = cv2.arcLength(cnt,True) # True for closed
            print(perimeter)

            # corner detection
            approx = cv2.approxPolyDP(cnt,0.02*perimeter,True)
            print(len(approx))
            objCor = len(approx)
            x, y, w, h =cv2.boundingRect(approx)

            #Shape detection
            if objCor ==3:objType ="Triangle"
            elif objCor==4:
                aspectRation = w/float(h)
                if aspectRation >0.95 and aspectRation <1.05:objType="Square"
                else:objType="Rect"
            elif objCor>4:objType="Circles"
            else:objType="None"


            cv2.rectangle(imgContour, (x,y),(x+w,y+h),(0,255,0),2)
            cv2.putText(imgContour,objType,
                        (x+(w//2)-10,y+(h//2)-10),
                        cv2.FONT_HERSHEY_COMPLEX,
                        0.7,(0,0,0),2)


path = 'Resources/shapes.png'
img =cv2.imread(path)
imgContour = img.copy()
imgGray= cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
imgBlur = cv2.GaussianBlur(imgGray,(7,7),1)
imgCanny= cv2.Canny(imgBlur,50,50)

getContours(imgCanny)

imgStack= si.stackImages(0.8,([img,imgGray,imgBlur],
                              [imgCanny,imgContour,img]))
cv2.imshow("OG",imgStack)
cv2.waitKey(0)