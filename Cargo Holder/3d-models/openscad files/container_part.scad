//------------------------------------------------------------------------------
// Cargo holder - container part
//
// This model contains all parts of the cargo holder mechanism for the cargo
// container, which can be attached to the drone via the drone_part.scad.
//
// This model is part of the AutonomousDroneDeliverySystem:
// https://github.com/Andreas-Menzel/AutonomousDroneDeliverySystem
//------------------------------------------------------------------------------
// @author: Andreas Menzel
// @copyright: Copyright (c) 2022 Andreas Menzel
//------------------------------------------------------------------------------


include <dimensions.scad>


module _container_part__alignment_pin() {
    // Short versions of the variabled needed
    width_base = alignment_pin_width_base;
    length_base = alignment_pin_length_base;
    width_top = alignment_pin_width_top;
    length_top = alignment_pin_length_top;
    height = alignment_pin_height;
    clearance = alignment_pin_clearance / 2;

    top_width_offset = (width_base - width_top) / 2;
    top_length_offset = (length_base - length_top) / 2;

    points = [
        // base
        [clearance, clearance, 0],
        [width_base - clearance, clearance, 0],
        [width_base - clearance, length_base - clearance, 0],
        [clearance, length_base - clearance, 0],

        // top
        // TODO: With this solution, the angles of the walls are slightly
        //       changed. This is no problem at all, but not very "beautiful",
        //       because I know that it isn't perfect.
        [top_width_offset + clearance, top_length_offset + clearance, height - clearance],
        [top_width_offset + width_top - clearance, top_length_offset + clearance, height - clearance],
        [top_width_offset + width_top - clearance, top_length_offset + length_top - clearance, height - clearance],
        [top_width_offset + clearance, top_length_offset + length_top - clearance, height - clearance]
    ];
    
    faces = [
        [0, 1, 2, 3], // bottom
        [7, 6, 5, 4], // top,

        [3, 7, 4, 0], // left
        [5, 6, 2, 1], // right

        [1, 0, 4, 5], // front
        [6, 7, 3, 2]  // back
    ];

    polyhedron(points, faces);
}


module _container_part__contact_plate() {
    // Short versions of the variabled needed
    width = contact_plate_width;
    length = contact_plate_length;
    wall_thickness = contact_plate_wall_thickness;

    cube([width, length, wall_thickness]);
}


module container_part() {
    union() {
        _container_part__contact_plate();

        translate([alignment_pin_offset, alignment_pin_offset, contact_plate_wall_thickness])
            _container_part__alignment_pin();
        translate([alignment_pin_offset, contact_plate_length - alignment_pin_length_base - alignment_pin_offset, contact_plate_wall_thickness])
            _container_part__alignment_pin();
    }
}


// When executing the `export.sh` script, this variable will autimatically be
// set to true. The default value should be false.
export = false;
if(export) {
    container_part();
}