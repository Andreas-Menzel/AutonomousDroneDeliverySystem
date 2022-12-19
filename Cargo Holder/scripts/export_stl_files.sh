#!/bin/bash

# This script is used to create the stl-files for the cargo holder mechanism.
# Make sure you have OpenSCAD installed and can use it to export models through
# the terminal.

mkdir -p "../3d-models/stl files"

openscad "../3d-models/openscad files/container_part.scad" -o "../3d-models/stl files/container_part.stl" -D "export=true;\$fn=50;"
openscad "../3d-models/openscad files/drone_part.scad" -o "../3d-models/stl files/drone_part.stl" -D "export=true;\$fn=50;"
openscad "../3d-models/openscad files/servo_mount.scad" -o "../3d-models/stl files/servo_mount.stl" -D "export=true;\$fn=50;"
openscad "../3d-models/openscad files/locking_pin.scad" -o "../3d-models/stl files/locking_pin.stl" -D "export=true;\$fn=50;"

openscad "../3d-models/openscad files/assembled.scad" -o "../3d-models/stl files/assembled.stl" -D "export=true;\$fn=50;"
