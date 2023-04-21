import cv2
import cv2 as cv

img = cv.imread('files/photos/cat.jpg')

# cv.imshow('Cat1', img)
# cv.waitKey(0)

capture = cv.VideoCapture('files/videos/DOG.mp4')
while True:
    isTrue, frame = capture.read()
    cv.imshow('Video', frame)

    if cv2.waitKey(20) & 0xFF == ord('d'):
        break

capture.release()
cv.destroyAllWindows()
cv2.waitKey(0)