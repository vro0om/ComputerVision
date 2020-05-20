import cv2
import numpy as np


img = np.zeros((512,512,3),np.uint8)
print(img)
# img[:] = 255,0,0 # whole image
#img[200:300,100:300] = 255,0,0 #selected area
height = img.shape[1]
width = img.shape[0]
cv2.line(img,(0,0),(height,width),(0,255,0),2)

cv2.rectangle(img, (20,20),(250,350),(0,0,255),2)
# cv2.rectangle(img, (250,350),(350,450),(0,0,255),cv2.FILLED)
cv2.circle(img,(450,350),30,(255,255,0),2)
cv2.putText(img,"Open Cv",(350,150),cv2.FONT_HERSHEY_SCRIPT_COMPLEX,1,(50,150,0),5)
cv2.imshow("Black",img)
cv2.waitKey(0)