import cv2
import numpy as np

img = cv2.imread("Resources/me.jpg")
print(img.shape)

imgResize= cv2.resize(img,(457,609)) #width , height
cv2.imshow("resized",imgResize)

imgCropped =img[400:600,200:500]
cv2.imshow("Cropped",imgCropped)

cv2.waitKey(0);