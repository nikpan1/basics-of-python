import math

import numpy as np
import cv2 as cv
import cv2.aruco as aruco


PATH = r'...'
img = cv.imread(PATH)
img = cv.resize(img, (1024, 576))
grayImg = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

DICT = aruco.Dictionary_get(aruco.DICT_4X4_50)
corners, ids, _ = aruco.detectMarkers(grayImg, DICT)

# IMG SHAPE ZWRACA NA ODWRÓT
mid_pos = int(img.shape[1]/2), int(img.shape[0]/2)

# to get one marker -> corners[0][0]
w = math.dist(corners[0][0][3], corners[0][0][0])
h = math.dist(corners[0][0][1], corners[0][0][2])

pts = np.asarray(corners[0][0], dtype=np.float32).reshape((-1, 1, 2))



# pts_dst = np.array([[0, 0], [w, 0], [h, w], [0, w]])
pts_dst = np.array([[0, 0], [w, 0], [h, w], [0, w]])


homography, status = cv.findHomography(pts, pts_dst, cv.RANSAC)
# dest_img = cv.warpPerspective(img, homography, (img.shape[0], img.shape[1]))

#pt = np.dot(homography, np.array([mid_pos[0], mid_pos[1], 1]))

pt = mid_pos  # your original point
px = (homography[0][0] * pt[0] + homography[0][1] * pt[1] + homography[0][2]) / \
     (homography[2][0] * pt[0] + homography[2][1] * pt[1] + homography[2][2])
py = (homography[1][0] * pt[0] + homography[1][1] * pt[1] + homography[1][2]) / \
     (homography[2][0] * pt[0] + homography[2][1] * pt[1] + homography[2][2])
pt = (int(px), int(py))  # after transformation

print(pts_dst)
print(f'homography:\n', homography)
print(f'midpos = ', mid_pos)
print(f'pt = ', (pt[0], pt[1]))
img = cv.circle(img, mid_pos, 4, (255, 0, 0), -1)
img = cv.circle(img, (int(pt[0]), int(pt[1])), 4, (0, 255, 0), -1)
cv.imshow("f", img)
cv.waitKey(0)

