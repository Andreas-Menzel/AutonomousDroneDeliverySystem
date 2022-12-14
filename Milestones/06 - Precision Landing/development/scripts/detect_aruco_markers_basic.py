# This script was downloaded from pyimagesearch.com and modified.
#
# Tutorial with the original version of this script:
# https://pyimagesearch.com/2020/12/21/detecting-aruco-markers-with-opencv-and-python/


from imutils.video import VideoStream
import imutils
import time
import cv2
import sys


ARUCO_TYPE = 'DICT_4X4_50'

IMAGE_WIDTH = 1000

VIDEO_SRC = '/dev/video2'


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

# Load the ArUCo dictionary and grab the ArUCo parameters
print(f"[INFO] detecting '{ARUCO_TYPE}' tags...")
arucoDict = cv2.aruco.Dictionary_get(ARUCO_DICT[ARUCO_TYPE])
arucoParams = cv2.aruco.DetectorParameters_create()

# Initialize the video stream and allow the camera sensor to warm up
print("[INFO] starting video stream...")
vs = VideoStream(src=VIDEO_SRC).start()
time.sleep(2.0)

# Loop over the frames from the video stream
while True:
	# Grab the frame from the threaded video stream and resize it to have a
    # maximum width of 1000 pixels
	frame = vs.read()
	frame = imutils.resize(frame, width=IMAGE_WIDTH)
	# Detect ArUco markers in the input frame
	(corners, ids, rejected) = cv2.aruco.detectMarkers(frame, arucoDict,
                                                       parameters=arucoParams)
    
    # Verify *at least* one ArUco marker was detected
	if len(corners) > 0:
		# Flatten the ArUco IDs list
		ids = ids.flatten()
		
        # Loop over the detected ArUCo corners
		for (markerCorner, markerID) in zip(corners, ids):
			# Extract the marker corners (which are always returned in top-left,
            # top-right, bottom-right, and bottom-left order)
			corners = markerCorner.reshape((4, 2))
			(topLeft, topRight, bottomRight, bottomLeft) = corners
			
            # Convert each of the (x, y)-coordinate pairs to integers
			topRight = (int(topRight[0]), int(topRight[1]))
			bottomRight = (int(bottomRight[0]), int(bottomRight[1]))
			bottomLeft = (int(bottomLeft[0]), int(bottomLeft[1]))
			topLeft = (int(topLeft[0]), int(topLeft[1]))

            # Draw the bounding box of the ArUCo detection
			cv2.line(frame, topLeft, topRight, (0, 255, 0), 2)
			cv2.line(frame, topRight, bottomRight, (0, 255, 0), 2)
			cv2.line(frame, bottomRight, bottomLeft, (0, 255, 0), 2)
			cv2.line(frame, bottomLeft, topLeft, (0, 255, 0), 2)
			# Compute and draw the center (x, y)-coordinates of the ArUco marker
			cX = int((topLeft[0] + bottomRight[0]) / 2.0)
			cY = int((topLeft[1] + bottomRight[1]) / 2.0)
			cv2.circle(frame, (cX, cY), 4, (0, 0, 255), -1)
			# Draw the ArUco marker ID on the frame
			cv2.putText(frame, str(markerID),
				(topLeft[0], topLeft[1] - 15),
				cv2.FONT_HERSHEY_SIMPLEX,
				0.5, (0, 255, 0), 2)

	# Show the output frame
	cv2.imshow("Frame", frame)
	key = cv2.waitKey(1) & 0xFF
	# if the `q` key was pressed, break from the loop
	if key == ord("q"):
		break

# do a bit of cleanup
cv2.destroyAllWindows()
vs.stop()