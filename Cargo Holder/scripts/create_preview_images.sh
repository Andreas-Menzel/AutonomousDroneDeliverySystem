#!/bin/bash

# This script creates preview images for all 3d models of the cargo holder.

mkdir -p ../images/

openscad "../3d-models/openscad files/container_part.scad" \
    -o "../images/container_part_preview.png" \
    -D "export=true;\$fn=50;" \
    --imgsize 800,600 \
    --autocenter --viewall \
    --render

openscad "../3d-models/openscad files/drone_part.scad" \
    -o "../images/drone_part_preview.png" \
    -D "export=true;\$fn=50;" \
    --imgsize 800,600 \
    --autocenter --viewall \
    --render

openscad "../3d-models/openscad files/servo_mount.scad" \
    -o "../images/servo_mount_preview.png" \
    -D "export=true;\$fn=50;" \
    --imgsize 800,600 \
    --autocenter --viewall \
    --render

openscad "../3d-models/openscad files/locking_pin.scad" \
    -o "../images/locking_pin_preview.png" \
    -D "export=true;\$fn=50;" \
    --imgsize 800,600 \
    --autocenter --viewall \
    --render

openscad "../3d-models/openscad files/assembled.scad" \
    -o "../images/assembled_preview.png" \
    -D "vertical_gap=150;\$fn=50;" \
    --imgsize 800,600 \
    --autocenter --viewall \
    --render