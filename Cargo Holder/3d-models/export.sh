#!/bin/bash

# This script is used to create the stl-files for the cargo holder mechanism.
# Make sure you have OpenSCAD installed and can use it via the terminal.

openscad "./openscad files/container_part.scad" -o "./stl files/container_part.stl" -D "export=true;"
openscad "./openscad files/drone_part.scad" -o "./stl files/drone_part.stl" -D "export=true;"

openscad "./openscad files/assembled.scad" -o "./stl files/assembled.stl" -D "export=true;"
