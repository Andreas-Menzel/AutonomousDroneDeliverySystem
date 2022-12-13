# 06 - Precision Landing

**Status:** work in progress

**Main Goal:** Precisely land the drone on a marker.

After completing this milestone, the drone should be able to precisely land on
a marker. This marker is later to be placed on the cargo station for further
development for the cargo pick-up and drop-off routines.

**To achive the main goal, the following tasks have to be finished:**

1. Create ArUco markers
2. Detect ArUco markers
3. Get relative position of ArUco marker / camera
4. Landing

## 1. Create ArUco markers

The first step is to create ArUco markers, so that they can be printed out and
detected by the drone.

We will use ArUco markers of type 4X4_50.

For this step, I slightly modified the script of
[this tutorial](https://pyimagesearch.com/2020/12/14/generating-aruco-markers-with-opencv-and-python/)
from [pyimagesearch.com](pyimagesearch.com).

The following will create ArUco markers of type `4X4_50` and save them to
`./development/images/ArUco markers/4X4_50/`:

```
cd development/scripts
python3 create_aruco_markers.py
```

**Make sure that your current directory is `./development/scrips/` when**
**executing the script or else it will create a new output folder for the**
**images.**

## 2. Detect ArUco markers

The first step is to create a python script that can detect ArUco markers using
the webcam.

The development of test scripts is done in `./development/`.
