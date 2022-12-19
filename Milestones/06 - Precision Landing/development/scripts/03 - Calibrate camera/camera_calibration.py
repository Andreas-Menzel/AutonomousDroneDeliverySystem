import numpy as np
import cv2
import imutils
from imutils.video import VideoStream
import time
import math
import json

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

time_next_snapshot = time.time() + 3
while True:
    frame = vs.read()
    frame = imutils.resize(frame, width=image_resolution[0], height=image_resolution[1])
    
    # Take next snapshot?
    if time.time() >= time_next_snapshot:
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Find the chess board corners
        ret, corners = cv2.findChessboardCorners(gray, (chessboard_size[0], chessboard_size[1]), None)
        
        # If found, add object points, image points (after refining them)
        if ret == True:
            objpoints.append(objp)
            corners2 = cv2.cornerSubPix(gray, corners, (11,11), (-1,-1), criteria)
            imgpoints.append(corners2)

            # Draw and display the corners
            cv2.drawChessboardCorners(frame, (chessboard_size[0], chessboard_size[1]), corners2, ret)
            cv2.imshow('Frame', frame)
            cv2.waitKey(500)
        
        time_next_snapshot = time.time() + 3

    cv2.putText(frame, 'Press "c" to stop taking snapshots and start calculating.',
                (30, 50),
                cv2.FONT_HERSHEY_SIMPLEX,
                1, (0, 255, 0), 2)

    cv2.putText(frame, f'Next snapshot in {math.ceil(time_next_snapshot - time.time())} second(s)...',
                (30, 150),
                cv2.FONT_HERSHEY_SIMPLEX,
                1, (0, 255, 0), 2)
    cv2.putText(frame, f'Valid snapshots taken: {len(objpoints)}',
                (30, 200),
                cv2.FONT_HERSHEY_SIMPLEX,
                1, (0, 255, 0), 2)
    cv2.imshow("Frame", frame)

    # if the `c` key was pressed, break from the loop
    key = cv2.waitKey(1) & 0xFF
    if key == ord("c"):
        break

cv2.destroyAllWindows()

if len(objpoints) > 0:
    if len(objpoints) < 5:
        print('At least 5 snapshot should be taken!')
    
    ret, mtx, dist, rvecs, tvecs = cv2.calibrateCamera(objpoints, imgpoints, gray.shape[::-1], None, None)

    camera_calibration_data = {
        'matrix': mtx.tolist(),
        'distortion': dist.tolist()
    }
    with open(f'camera_calibration_{image_resolution[0]}x{image_resolution[1]}.json', 'w') as file:
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