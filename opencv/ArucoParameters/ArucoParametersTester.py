# moduł testujący parametry ustawione do detekcji

import numpy as np
import cv2 as cv
import cv2.aruco as aruco

import os
from tqdm import tqdm

DIR = 'imgs'
RESOLUTION = 1024, 576
grayscale = False
DICT = aruco.Dictionary_get(aruco.DICT_4X4_50)
params = aruco.DetectorParameters_create()


def detectAruco(img):
    if grayscale:
        img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    corners, ids, rejected = aruco.detectMarkers(img, DICT, parameters=params)
    result = [0, 0]

    try:
        result[0] = len(corners)
    except:
        result[0] = 0

    try:
        result[1] = len(rejected)
    except:
        result[1] = 0

    return result


if __name__ == '__main__':
    osList = os.listdir(DIR)
    osAmount = len(osList)
    collectedData = np.zeros((osAmount, 2), np.int16)

    for filename, index in tqdm(zip(osList, range(0, osAmount))):
        path = os.path.join(os.getcwd(), DIR, filename)
        img = cv.imread(path)
        img = cv.resize(img, RESOLUTION)
        collectedData[index][0], collectedData[index][1] = detectAruco(img)

    unique_val, amount_val = np.unique(collectedData[:, 0], return_counts=True)
    print("unique_val - ", unique_val)  # jakie wartości znalezione
    print("amount_val - ", amount_val)  # ile takich wartości było
    print("rejected_avg - ", np.average(collectedData[:, 1]))