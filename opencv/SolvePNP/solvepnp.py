import numpy as np
import cv2 as cv
import cv2.aruco as aruco
import yaml
from yaml.loader import SafeLoader


DICT = aruco.Dictionary_get(aruco.DICT_4X4_50)
PARAM =  aruco.DetectorParameters_create()
PARAM.adaptiveThreshWinSizeMin = 100  # default 3
PARAM.adaptiveThreshWinSizeMax = 300  # default 23
PARAM.adaptiveThreshWinSizeStep = 30  # default 10
PARAM.adaptiveThreshConstant = 5      # default 7
PARAM.perspectiveRemoveIgnoredMarginPerCell = 0.35 # default 0.13
PARAM.minDistanceToBorder = 1  # default  3
PARAM.cornerRefinementMaxIterations = 60  # default 30


def rotate(img, dgr):
    img = cv.rotate(img, cv.ROTATE_90_CLOCKWISE)
    new_img = np.zeros((900, 900, 3), dtype=np.uint8)
    x_offset, y_offset = 0, 50
    new_img[y_offset:y_offset+img.shape[0], x_offset:x_offset+img.shape[1]] = img
    return new_img

def calib():
    with open('calibration.yaml') as f:
        loadeddict = yaml.load(f, Loader=SafeLoader)
    mtx = loadeddict.get('camera_matrix')
    dist = loadeddict.get('dist_coeff')
    mtx = np.array(mtx)
    dist = np.array(dist)
    return mtx, dist

def distort(img):
    h, w = img.shape[:2]
    newCamMatrix, roi = cv.getOptimalNewCameraMatrix(mtx, dist, (w, h), 1, (w, h))
    mapx, mapy = cv.initUndistortRectifyMap(mtx, dist, None, newCamMatrix, (w,h), 5)  # undistortion
    dst = cv.remap(img, mapx, mapy, cv.INTER_LINEAR)
    x, y, w, h = roi
    dst = dst[y:y+h, x:x+w]
    return dst


PATH = r'A:\_Pens\Minerwa\ArucoVisual\mins\3.jpg'
mtx, dist = calib()

img = cv.imread(PATH)
img = distort(img)
img = rotate(img, 3)
cv.imshow("Title", img)
cv.waitKey(0)
corners, ids, rej = aruco.detectMarkers(img, DICT, parameters=PARAM)
print(ids)
aruco.drawDetectedMarkers(img, corners)
#aruco.drawDetectedMarkers(img, rej)  # draw rejected corners
corners = np.squeeze(corners)
print(corners)
TLcorner3D = np.array([
    (0.0, 0.0, 0.0),
    (100.0, 0.0, 0.0),
    (100.0, 100.0, 0.0),
    (0.0, 100.0, 0.0)
], dtype="double")

TDcorner3D = np.array([
    (0.0, 389.0, 0.0),
    (100.0, 389.0, 0.0),
    (100.0, 489.0, 0.0),
    (0.0, 489.0, 0.0)
], dtype="double")

points_2D = np.array(np.concatenate((corners[0], corners[1]), axis=0), dtype="double")
points_3D = np.array(np.concatenate((TDcorner3D, TLcorner3D), axis=0), dtype="double")
"""points_2D = np.array(corners[1], dtype="double")
points_3D = np.array(TLcorner3D, dtype="double")"""
print(points_2D, "\n", points_3D)

scs, rvec, tvec = cv.solvePnP(points_3D, points_2D, mtx, dist, flags=0)  # SOLVE PNP

# projected X lines
for i in range(0, 23):
    p1, jacobian = cv.projectPoints(np.array([(50.0 * i, 0.0, 0.0)]), rvec, tvec, mtx, dist)
    p2, jacobian = cv.projectPoints(np.array([(50.0 * i, 1300.0, 0.0)]), rvec, tvec, mtx, dist)
    p1 = np.squeeze(p1)
    p2 = np.squeeze(p2)
    img = cv.line(img, (int(p2[0]), int(p2[1])), (int(p1[0]), int(p1[1])), (0, 100, 255), 1)

# projected Y lines
for i in range(0, 13):
    p1, jacobian = cv.projectPoints(np.array([(0.0, 50.0 * i, 0.0)]), rvec, tvec, mtx, dist)
    p2, jacobian = cv.projectPoints(np.array([(1400.0, 50.0 * i, 0.0)]), rvec, tvec, mtx, dist)
    p1 = np.squeeze(p1)
    p2 = np.squeeze(p2)
    img = cv.line(img, (int(p2[0]), int(p2[1])), (int(p1[0]), int(p1[1])), (0, 100, 255), 1)

p, jacobian = cv.projectPoints(np.array([(0.0, 489.0, 0.0)]), rvec, tvec, mtx, dist)
p = np.squeeze(p)
cv.circle(img, (int(p[0]), int(p[1])), 4, (255,0,200), -1)

p, jacobian = cv.projectPoints(np.array([(890.0, 0.0, 0.0)]), rvec, tvec, mtx, dist)
p = np.squeeze(p)
cv.circle(img, (int(p[0]), int(p[1])), 4, (255,0,200), -1)

cv.imshow("Title", img)
cv.waitKey(0)
