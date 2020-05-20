import cv2

# image
# from pip._internal.req.req_file import ignore_comments
#
# print("package imported")
#
# img = cv2.imread("Resources/zoya.jpg")
#
# cv2.imshow("Output",img)
# cv2.waitKey(0)
# ignore_comments()


# Video
# videoCapture = cv2.VideoCapture("Resources/viddance.mp4")
#
# while True:
#     success, img = videoCapture.read()
#     cv2.imshow("Video",img)
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break

# Web cam

videoCapture = cv2.VideoCapture(0)
videoCapture.set(3,640)
videoCapture.set(4,480)
videoCapture.set(10,100)
while True:
    success, img = videoCapture.read()
    cv2.imshow("Video",img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break