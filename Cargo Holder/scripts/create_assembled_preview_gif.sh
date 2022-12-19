#!/bin/bash

# This script creates an animated gif of the assembled cargo holder mechanism.

mkdir -p .tmp_assembled_preview_gif

for vertical_gap in {000..150..1}
do
    openscad "../3d-models/openscad files/assembled.scad" -o ".tmp_assembled_preview_gif/assembled_$vertical_gap.png" -D "vertical_gap=$vertical_gap;\$fn=50;" --imgsize 800,600 --camera 80,71,83,52,0,57,718 --render
done

mkdir -p ../images/
convert -delay 2 -loop 0 .tmp_assembled_preview_gif/*.png ../images/assembled_preview.gif

rm -R .tmp_assembled_preview_gif
