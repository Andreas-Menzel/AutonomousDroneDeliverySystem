# This script was downloaded from pyimagesearch.com and modified.
#
# Tutorial with the original version of this script:
# https://pyimagesearch.com/2020/12/14/generating-aruco-markers-with-opencv-and-python/

import numpy as np
import cv2
import sys
from pathlib import Path

ARUCO_TYPE = 'DICT_4X4_50'
OUTPUT_IMG_SIZE = 300


ARUCO_DICT = {
    'DICT_4X4_50': cv2.aruco.DICT_4X4_50,
    'DICT_4X4_100': cv2.aruco.DICT_4X4_100,
    'DICT_4X4_250': cv2.aruco.DICT_4X4_250,
    'DICT_4X4_1000': cv2.aruco.DICT_4X4_1000,
    'DICT_5X5_50': cv2.aruco.DICT_5X5_50,
    'DICT_5X5_100': cv2.aruco.DICT_5X5_100,
    'DICT_5X5_250': cv2.aruco.DICT_5X5_250,
    'DICT_5X5_1000': cv2.aruco.DICT_5X5_1000,
    'DICT_6X6_50': cv2.aruco.DICT_6X6_50,
    'DICT_6X6_100': cv2.aruco.DICT_6X6_100,
    'DICT_6X6_250': cv2.aruco.DICT_6X6_250,
    'DICT_6X6_1000': cv2.aruco.DICT_6X6_1000,
    'DICT_7X7_50': cv2.aruco.DICT_7X7_50,
    'DICT_7X7_100': cv2.aruco.DICT_7X7_100,
    'DICT_7X7_250': cv2.aruco.DICT_7X7_250,
    'DICT_7X7_1000': cv2.aruco.DICT_7X7_1000,
    'DICT_ARUCO_ORIGINAL': cv2.aruco.DICT_ARUCO_ORIGINAL,
    'DICT_APRILTAG_16h5': cv2.aruco.DICT_APRILTAG_16h5,
    'DICT_APRILTAG_25h9': cv2.aruco.DICT_APRILTAG_25h9,
    'DICT_APRILTAG_36h10': cv2.aruco.DICT_APRILTAG_36h10,
    'DICT_APRILTAG_36h11': cv2.aruco.DICT_APRILTAG_36h11
}

# verify that the supplied ArUCo tag exists and is supported by OpenCV
if ARUCO_DICT.get(ARUCO_TYPE, None) is None:
    print(f'[INFO] ArUCo tag of "{ARUCO_TYPE}" is not supported')
    sys.exit(0)

# Load the ArUCo dictionary
arucoDict = cv2.aruco.Dictionary_get(ARUCO_DICT[ARUCO_TYPE])

# Allocate memory for the output ArUCo tag and then draw the ArUCo tag on the
# output image
Path(f'../images/ArUco markers/{ARUCO_TYPE.split("_", 1)[1]}/').mkdir(parents=True, exist_ok=True)
tag = np.zeros((OUTPUT_IMG_SIZE, OUTPUT_IMG_SIZE, 1), dtype="uint8")
for aruco_id in range(0, int(ARUCO_TYPE.split('_')[-1])):
    print(f'[INFO] generating ArUCo tag type "{ARUCO_TYPE}" with ID "{aruco_id}"')
    cv2.aruco.drawMarker(arucoDict, aruco_id, OUTPUT_IMG_SIZE, tag, 1)
    cv2.imwrite(f'../images/ArUco markers/{ARUCO_TYPE.split("_", 1)[1]}/{OUTPUT_IMG_SIZE}x{OUTPUT_IMG_SIZE}_{aruco_id}.png', tag)
