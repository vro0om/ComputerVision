import cv2
import numpy as np

img = cv2.imread("Resources/zoya.jpg")
imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
imgRed = cv2.cvtColor(img,cv2.COLOR_BGR2BGR555)

hor1 = np.hstack((img,img,img))
hor2 = np.hstack((img,img,img))
vert= np.vstack((hor1,hor2))
# cv2.imshow("Hor",hor)
cv2.imshow("ver",vert)
cv2.imshow("gr",imgGray)

cv2.waitKey(0)