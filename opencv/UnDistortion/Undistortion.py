import numpy as np
import cv2
import cv2.aruco as aruco
import os
import pickle
import yaml
from yaml.loader import SafeLoader


with open('calibration.yaml') as f:
    loadeddict = yaml.load(f, Loader=SafeLoader)
mtx = loadeddict.get('camera_matrix')
dist = loadeddict.get('dist_coeff')
mtx = np.array(mtx)
dist = np.array(dist)

img = cv2.imread(r'C:\Users\Nikodem\Documents\GitHub\camera_calibration\imgs\3-11-2022-23-5-10.jpg')
print(img.shape)
w = img.shape[1]
h = img.shape[0]


newCamMatrix, roi = cv2.getOptimalNewCameraMatrix(mtx, dist, (w, h), 1, (w, h))
mapx, mapy = cv2.initUndistortRectifyMap(mtx, dist, None, newCamMatrix, (w,h), 5)  # undistortion
dst = cv2.remap(img, mapx, mapy, cv2.INTER_LINEAR)

# crop the image
x, y, w, h = roi
dst = dst[y:y+h, x:x+w]


cv2.imshow("przed", img)
cv2.waitKey(0)
cv2.imshow("po", dst)
cv2.waitKey(0)
