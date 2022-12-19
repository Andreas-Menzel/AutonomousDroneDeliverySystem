import numpy as np
import cv2
import imutils
from imutils.video import VideoStream
import time

################################################################################
############################ CHANGE THESE VARIABLES ############################
################################################################################

chessboard_size = (10, 7)

video_source = '/dev/video2'
image_resolution = (1280, 720)

################################################################################
######################## DO NOT CHANGE THESE VARIABLES #########################
################################################################################

# Termination criteria
criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 30, 0.001)

# Prepare object points, like (0,0,0), (1,0,0), (2,0,0) ....,(6,5,0)
objp = np.zeros((chessboard_size[0]*chessboard_size[1],3), np.float32)
objp[:,:2] = np.mgrid[0:chessboard_size[0],0:chessboard_size[1]].T.reshape(-1,2)

# Arrays to store object points and image points from all the images.
objpoints = [] # 3d point in real world space
imgpoints = [] # 2d points in image plane.


vs = VideoStream(src=video_source).start()
time.sleep(2.0)

while True:
    frame = vs.read()
    frame = imutils.resize(frame, width=image_resolution[0], height=image_resolution[1])

    key = cv2.waitKey(1) & 0xFF
    if key == ord("s"):
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Find the chess board corners
        ret, corners = cv2.findChessboardCorners(gray, (chessboard_size[0], chessboard_size[1]), None)
        
        # If found, add object points, image points (after refining them)
        if ret == True:
            print('Chessboard found!')

            objpoints.append(objp)
            corners2 = cv2.cornerSubPix(gray, corners, (11,11), (-1,-1), criteria)
            imgpoints.append(corners2)

            # Draw and display the corners
            cv2.drawChessboardCorners(frame, (chessboard_size[0], chessboard_size[1]), corners2, ret)
            cv2.imshow('Frame', frame)
            cv2.waitKey(500)

    cv2.imshow("Frame", frame)
    # if the `q` key was pressed, break from the loop
    if key == ord("q"):
        break

cv2.destroyAllWindows()

ret, mtx, dist, rvecs, tvecs = cv2.calibrateCamera(objpoints, imgpoints, gray.shape[::-1], None, None)

print(mtx)
print(dist)
print(rvecs)
print(tvecs)