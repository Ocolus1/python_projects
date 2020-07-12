import cv2, time

# it uses the web cam to take photos every five seconds
video = cv2.VideoCapture(0)
while True:
    check, frame = video.read()
    grey = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    cv2.imshow("Master", grey)
    cv2.waitKey(0)
    time.sleep(5)

video.release()
cv2.destroyAllWindows()






# import cv2
# # To read the an image
# img = cv2.imread("shot.jpg", 1)
# # To open image
# # img = cv2.imread("shot.jpg", 1) => color image
# # img = cv2.imread("shot.jpg", 0) => black and white image 

# # shape of image
# print(img.shape)

# # Resize image
# img = cv2.resize(img, (300,300))

# cv2.imshow("Master", img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
