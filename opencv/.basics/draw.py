import cv2 as cv
import numpy as np

blank = np.zeros((500, 500, 3), dtype = 'uint8')
cv.imshow('Blank', blank)

#paint the image a certain colour
blank[200:300, 300:400] = 0, 255, 0
cv.imshow('Green', blank)

# draw a rectangle
cv.rectangle(blank, (0,0), (255, 255), (0, 255, 0), thickness=2)
cv.imshow('Rectangle', blank)
cv.waitKey(0)