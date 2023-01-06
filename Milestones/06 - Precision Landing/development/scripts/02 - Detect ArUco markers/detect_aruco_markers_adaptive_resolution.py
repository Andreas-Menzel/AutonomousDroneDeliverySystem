import imutils
import time
import cv2
import sys
from scipy.spatial import distance

from AdvancedVideoStream import AdvancedVideoStream


################################################################################
############################ CHANGE THESE VARIABLES ############################
################################################################################

# Set depending on the ArUco type that should be detected
ARUCO_TYPE = 'DICT_4X4_50'

# Preferred size (in px) of a marker. Should be a value so that the markers
# can be easily detected, but not too high in order to reduce the image size and
# processing required to find the markers.
PREFERRED_MARKER_SIZE = 75

# Width of the image (in px). Should not be too high (max: camera resolution)
# in order to reduce the processing required to find a marker. Min-size is not
# too important, unless there is a very big and a very small maker and both
# should be detected (only important if the small marker comes into view after
# the big marker).
IMG_WIDTH_MIN = 50
IMG_WIDTH_MAX = 2500

# Video source. Either a webcam (/dev/videoX) or a file (e.g. video.mp4)
VIDEO_SRC = '/dev/video3'
#VIDEO_SRC = './video.mp4'

# Maximum fps of the livestream | fps of the video
VIDEO_FPS = 30

# With of the preview image (in px)
IMG_DISPLAY_WIDTH = 1000

################################################################################
######################## DO NOT CHANGE THESE VARIABLES #########################
################################################################################

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

# Sizes of all markers currently detected
marker_sizes = []
# Current image width
image_width = IMG_WIDTH_MAX

# Verify that the supplied ArUCo tag exists and is supported by OpenCV
if ARUCO_DICT.get(ARUCO_TYPE, None) is None:
    print(f"[INFO] ArUCo tag of '{ARUCO_TYPE}' is not supported.")
    sys.exit(0)

# Load the ArUCo dictionary and grab the ArUCo parameters
print(f"[INFO] detecting '{ARUCO_TYPE}' tags...")
arucoDict = cv2.aruco.Dictionary_get(ARUCO_DICT[ARUCO_TYPE])
arucoParams = cv2.aruco.DetectorParameters_create()

# Initialize the video stream or file
print("[INFO] starting video stream or file...")
vs = AdvancedVideoStream(VIDEO_SRC, fps=VIDEO_FPS)
vs.start()

time_last_frame = round(time.time()*1000) - 1000 # actually the 5th latest frame
frame_rate = 1 # will be calculated and updated
frames_counter = 0
# Loop over the frames from the video stream
while True:
    if not vs.is_active():
        print('Video stream is not active.')
        break

    smallest_marker_size = 0
    if len(marker_sizes) > 0:
        smallest_marker_size = min(marker_sizes)
    marker_sizes = []
    
    frames_counter = frames_counter + 1

    if smallest_marker_size == 0:
        # Set max-resolution
        image_width = IMG_WIDTH_MAX
    else:
        # Scale image
        scaling_factor = (PREFERRED_MARKER_SIZE) / smallest_marker_size
        
        image_width = int(image_width * scaling_factor)
        if image_width > IMG_WIDTH_MAX:
            image_width = IMG_WIDTH_MAX
        elif image_width < IMG_WIDTH_MIN:
            image_width = IMG_WIDTH_MIN

    # Grab the frame from the threaded video stream and resize it
    frame = vs.get_frame()
    frame = imutils.resize(frame, width=image_width)

    # Convert to grayscale: improves efficiency
    #frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

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
            
            # Get and set the smallest marker size
            size_top = distance.euclidean(topLeft, topRight)
            size_bottom = distance.euclidean(bottomLeft, bottomRight)
            size_left = distance.euclidean(topLeft, bottomLeft)
            size_right = distance.euclidean(topRight, bottomRight)

            smallest_size = int(min(size_top, size_bottom, size_left, size_right))
            marker_sizes.append(smallest_size)

    # Update smallest_marker_size now that we have detected the markers
    smallest_marker_size = 0
    if len(marker_sizes) > 0:
        smallest_marker_size = min(marker_sizes)

    # Calculate frame rate every 5 frames
    if frames_counter % 5 == 0:
        frames_counter = 0
        frame_rate = 1000 / (round(time.time()*1000) - time_last_frame)
        time_last_frame = round(time.time()*1000)

    # Show the output frame
    frame = imutils.resize(frame, width=IMG_DISPLAY_WIDTH)

    # Show help message
    cv2.putText(frame, 'Press "q" to quit.', (30, 50),
				cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

    cv2.putText(frame, f'FPS: {round(frame_rate, 2)}', (30, 100), cv2.FONT_HERSHEY_SIMPLEX,
                1, (0, 255, 0), 2)
    cv2.putText(frame, int(frame_rate / 2)*'#', (30, 150), cv2.FONT_HERSHEY_SIMPLEX,
                1, (0, 255, 0), 2)

    cv2.putText(frame, f'Smallest marker size: {round(smallest_marker_size)}px', (30, 250), cv2.FONT_HERSHEY_SIMPLEX,
                1, (0, 255, 0), 2)
    marker_sizes_str = 'px, '.join([ str(elem) for elem in sorted(marker_sizes) ])
    cv2.putText(frame, f'All marker sizes: {marker_sizes_str}px', (30, 300), cv2.FONT_HERSHEY_SIMPLEX,
                1, (0, 255, 0), 2)

    cv2.imshow("Frame", frame)
    key = cv2.waitKey(1) & 0xFF
    # if the `q` key was pressed, break from the loop
    if key == ord("q"):
        break

# do a bit of cleanup
cv2.destroyAllWindows()
vs.stop()
print(f'Total number of input frames: {vs.frames_count}')
