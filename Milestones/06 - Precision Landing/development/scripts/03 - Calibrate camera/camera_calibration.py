import numpy as np
import cv2
import imutils
import time
import math
import json

from AdvancedVideoStream import AdvancedVideoStream


################################################################################
############################ CHANGE THESE VARIABLES ############################
################################################################################

CHESSBOARD_SIZE = (10, 7)

# Video source. Either a webcam (/dev/videoX) or a file (e.g. video.mp4)
#VIDEO_SRC = '/dev/video3'
VIDEO_SRC = '../../videos/ChArUco_board.mp4'

# Maximum fps of the livestream | fps of the video
VIDEO_FPS = 30

IMG_RESOLUTION = (1280, 720)

################################################################################
######################## DO NOT CHANGE THESE VARIABLES #########################
################################################################################

# Termination criteria
criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 30, 0.001)

# Prepare object points, like (0,0,0), (1,0,0), (2,0,0) ....,(6,5,0)
objp = np.zeros((CHESSBOARD_SIZE[0]*CHESSBOARD_SIZE[1],3), np.float32)
objp[:,:2] = np.mgrid[0:CHESSBOARD_SIZE[0],0:CHESSBOARD_SIZE[1]].T.reshape(-1,2)

# Arrays to store object points and image points from all the images.
objpoints = [] # 3d point in real world space
imgpoints = [] # 2d points in image plane.

# Initialize the video stream or file
print("[INFO] starting video stream or file...")
vs = AdvancedVideoStream(VIDEO_SRC, fps=VIDEO_FPS)
vs.start()

time_next_snapshot = time.time() + 3
while True:
    key = cv2.waitKey(1) & 0xFF

    frame = vs.get_frame()
    frame = imutils.resize(frame, width=IMG_RESOLUTION[0], height=IMG_RESOLUTION[1])
    
    # Take next snapshot?
    if time.time() >= time_next_snapshot or key == ord('s'):
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Find the chess board corners
        ret, corners = cv2.findChessboardCorners(gray, (CHESSBOARD_SIZE[0], CHESSBOARD_SIZE[1]), None)
        
        # If found, add object points, image points (after refining them)
        if ret == True:
            objpoints.append(objp)
            corners2 = cv2.cornerSubPix(gray, corners, (11,11), (-1,-1), criteria)
            imgpoints.append(corners2)

            # Draw and display the corners
            cv2.drawChessboardCorners(frame, (CHESSBOARD_SIZE[0], CHESSBOARD_SIZE[1]), corners2, ret)
            cv2.imshow('Frame', frame)
            cv2.waitKey(500)
        
        time_next_snapshot = time.time() + 3

    cv2.putText(frame, 'Press "c" to stop taking snapshots and start calculating.',
                (30, 50),
                cv2.FONT_HERSHEY_SIMPLEX,
                1, (0, 255, 0), 2)
    cv2.putText(frame, 'Press "s" to take a snapshot.',
                (30, 100),
                cv2.FONT_HERSHEY_SIMPLEX,
                1, (0, 255, 0), 2)

    cv2.putText(frame, f'Next snapshot in {math.ceil(time_next_snapshot - time.time())} second(s)...',
                (30, 200),
                cv2.FONT_HERSHEY_SIMPLEX,
                1, (0, 255, 0), 2)
    cv2.putText(frame, f'Valid snapshots taken: {len(objpoints)}',
                (30, 250),
                cv2.FONT_HERSHEY_SIMPLEX,
                1, (0, 255, 0), 2)
    cv2.imshow("Frame", frame)

    # if the `c` key was pressed, break from the loop
    if key == ord('c'):
        break

cv2.destroyAllWindows()
vs.stop()

if len(objpoints) > 0:
    if len(objpoints) < 5:
        print('At least 5 snapshot should be taken!')
    
    ret, mtx, dist, rvecs, tvecs = cv2.calibrateCamera(objpoints, imgpoints, gray.shape[::-1], None, None)

    camera_calibration_data = {
        'matrix': mtx.tolist(),
        'distortion': dist.tolist()
    }
    with open('camera_calibration_matrix.npy', 'wb') as file:
        np.save(file, mtx)
    with open('camera_calibration_distortion.npy', 'wb') as file:
        np.save(file, dist)

    with open(f'camera_calibration_{IMG_RESOLUTION[0]}x{IMG_RESOLUTION[1]}.json', 'w') as file:
        file.write(json.dumps(camera_calibration_data))
        print(f'Matrix:\n{mtx}')
        print(f'Distortion:\n{dist}')

    mean_error = 0
    for i in range(len(objpoints)):
        imgpoints2, _ = cv2.projectPoints(objpoints[i], rvecs[i], tvecs[i], mtx, dist)
        error = cv2.norm(imgpoints[i], imgpoints2, cv2.NORM_L2)/len(imgpoints2)
        mean_error += error
    print(f'Total error: {mean_error/len(objpoints)}')
else:
    print('At least one snapshot must be taken!')