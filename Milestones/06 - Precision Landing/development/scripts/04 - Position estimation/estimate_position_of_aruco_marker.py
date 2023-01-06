# This script was downloaded from Github and modified.
#
# The original version of this script:
# https://github.com/Asadullah-Dal17/Basic-Augmented-reality-course-opencv/blob/master/DISTANCE-ESTIMATION/distance.py


import cv2 as cv2
from cv2 import aruco
import numpy as np
import imutils
import time

from AdvancedVideoStream import AdvancedVideoStream


################################################################################
############################ CHANGE THESE VARIABLES ############################
################################################################################

ARUCO_TYPE = 'DICT_4X4_50'

# Size of the marker in real life (in cm; input unit = output unit)
MARKER_SIZE = 16

# Video source. Either a webcam (/dev/videoX) or a file (e.g. video.mp4)
VIDEO_SRC = '/dev/video3'
#VIDEO_SRC = 'video.mp4'

# Maximum fps of the livestream | fps of the video
VIDEO_FPS = 30

# Paths to the calibration files generated in the previous step
# (03 - Calibrate camera)
CAMERA_CALIBRATION_FILE_MATRIX = 'camera_calibration_matrix.npy'
CAMERA_CALIBRATION_FILE_DISTORTION = 'camera_calibration_distortion.npy'

################################################################################
######################## DO NOT CHANGE THESE VARIABLES #########################
################################################################################


# Define names of each possible ArUco tag OpenCV supports
ARUCO_DICT = {
	"DICT_4X4_50": cv2.aruco.DICT_4X4_50,
	"DICT_4X4_100": cv2.aruco.DICT_4X4_100,
	"DICT_4X4_250": cv2.aruco.DICT_4X4_250,
	"DICT_4X4_1000": cv2.aruco.DICT_4X4_1000,
	"DICT_5X5_50": cv2.aruco.DICT_5X5_50,
	"DICT_5X5_100": cv2.aruco.DICT_5X5_100,
	"DICT_5X5_250": cv2.aruco.DICT_5X5_250,
	"DICT_5X5_1000": cv2.aruco.DICT_5X5_1000,
	"DICT_6X6_50": cv2.aruco.DICT_6X6_50,
	"DICT_6X6_100": cv2.aruco.DICT_6X6_100,
	"DICT_6X6_250": cv2.aruco.DICT_6X6_250,
	"DICT_6X6_1000": cv2.aruco.DICT_6X6_1000,
	"DICT_7X7_50": cv2.aruco.DICT_7X7_50,
	"DICT_7X7_100": cv2.aruco.DICT_7X7_100,
	"DICT_7X7_250": cv2.aruco.DICT_7X7_250,
	"DICT_7X7_1000": cv2.aruco.DICT_7X7_1000,
	"DICT_ARUCO_ORIGINAL": cv2.aruco.DICT_ARUCO_ORIGINAL,
	"DICT_APRILTAG_16h5": cv2.aruco.DICT_APRILTAG_16h5,
	"DICT_APRILTAG_25h9": cv2.aruco.DICT_APRILTAG_25h9,
	"DICT_APRILTAG_36h10": cv2.aruco.DICT_APRILTAG_36h10,
	"DICT_APRILTAG_36h11": cv2.aruco.DICT_APRILTAG_36h11
}

# Verify that the supplied ArUCo tag exists and is supported by OpenCV
if ARUCO_DICT.get(ARUCO_TYPE, None) is None:
	print(f"[INFO] ArUCo tag of '{ARUCO_TYPE}' is not supported.")
	sys.exit(0)

marker_type = ARUCO_DICT[ARUCO_TYPE]

# Load numpy calibration files
cam_mat = np.load(CAMERA_CALIBRATION_FILE_MATRIX)
dist_coef = np.load(CAMERA_CALIBRATION_FILE_DISTORTION)

marker_dict = aruco.Dictionary_get(marker_type)

param_markers = aruco.DetectorParameters_create()

# Initialize the video stream or file
print("[INFO] starting video stream or file...")
vs = AdvancedVideoStream(VIDEO_SRC, fps=VIDEO_FPS)
vs.start()

while True:
    frame = vs.get_frame()
    frame = imutils.resize(frame, width=1280, height=720)

    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    marker_corners, marker_IDs, reject = aruco.detectMarkers(gray_frame,
                                                             marker_dict,
                                                             parameters=param_markers)
    if marker_corners:
        rVec, tVec, _ = aruco.estimatePoseSingleMarkers(marker_corners,
                                                        MARKER_SIZE, cam_mat,
                                                        dist_coef)
        total_markers = range(0, marker_IDs.size)
        for ids, corners, i in zip(marker_IDs, marker_corners, total_markers):
            cv2.polylines(frame, [corners.astype(np.int32)], True,
                          (0, 255, 255), 4, cv2.LINE_AA)
            corners = corners.reshape(4, 2)
            corners = corners.astype(int)
            
            top_right = corners[0].ravel()
            top_left = corners[1].ravel()
            bottom_right = corners[2].ravel()
            bottom_left = corners[3].ravel()

            distance = np.sqrt(
                tVec[i][0][2] ** 2 + tVec[i][0][0] ** 2 + tVec[i][0][1] ** 2
            )
            
            # Draw the pose of the marker
            point = cv2.drawFrameAxes(frame, cam_mat, dist_coef, rVec[i], tVec[i], 4, 4)
            cv2.putText(
                frame,
                f"id: {ids[0]} Dist: {round(distance, 2)}",
                top_right,
                cv2.FONT_HERSHEY_PLAIN,
                2,
                (0, 0, 255),
                2,
                cv2.LINE_AA,
            )
            cv2.putText(
                frame,
                f"x:{round(tVec[i][0][0],1)} y: {round(tVec[i][0][1],1)} ",
                bottom_right,
                cv2.FONT_HERSHEY_PLAIN,
                1.0,
                (0, 0, 255),
                2,
                cv2.LINE_AA,
            )
    
    # Show help message
    cv2.putText(frame, 'Press "q" to quit.', (30, 50),
				cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

    cv2.imshow("frame", frame)
    key = cv2.waitKey(1)
    if key == ord("q"):
        break

# Do a bit of cleanup
cv2.destroyAllWindows()
vs.stop()
