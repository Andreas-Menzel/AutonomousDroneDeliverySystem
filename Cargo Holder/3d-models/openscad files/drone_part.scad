//------------------------------------------------------------------------------
// Cargo holder - drone part
//
// This model contains all parts of the cargo holder mechanism mounted directly
// to the drone.
//
// This model is part of the AutonomousDroneDeliverySystem:
// https://github.com/Andreas-Menzel/AutonomousDroneDeliverySystem
//------------------------------------------------------------------------------
// @author: Andreas Menzel
// @copyright: Copyright (c) 2022 Andreas Menzel
//------------------------------------------------------------------------------


include <dimensions.scad>


module _drone_part__alignment_pin_slot() {
    // Short versions of the variabled needed
    width_base = alignment_pin_width_base;
    length_base = alignment_pin_length_base;
    width_top = alignment_pin_width_top;
    length_top = alignment_pin_length_top;
    height = alignment_pin_height;
    clearance = alignment_pin_clearance / 2;

    plane_wall_thickness = alignment_pin_slot_plane_wall_thickness;
    wall_thickness = alignment_pin_slot_wall_thickness;

    top_width_offset = (width_base - width_top) / 2;
    top_length_offset = (length_base - length_top) / 2;

    points = [
        // base - inner
        [-clearance, -clearance, 0],
        [width_base + clearance, -clearance, 0],
        [width_base + clearance, length_base + clearance, 0],
        [-clearance, length_base + clearance, 0],

        // base - outer
        [-clearance - plane_wall_thickness, -clearance - plane_wall_thickness, 0],
        [width_base + clearance + plane_wall_thickness, -clearance - plane_wall_thickness, 0],
        [width_base + clearance + plane_wall_thickness, length_base + clearance + plane_wall_thickness, 0],
        [-clearance  -plane_wall_thickness, length_base + clearance + plane_wall_thickness, 0],

        // top - inner
        // TODO: With this solution, the angles of the walls are slightly
        //       changed. This is no problem at all, but not very "beautiful",
        //       because I know that it isn't perfect.
        [top_width_offset - clearance, top_length_offset - clearance, height + clearance],
        [top_width_offset + width_top + clearance, top_length_offset - clearance, height + clearance],
        [top_width_offset + width_top + clearance, top_length_offset + length_top + clearance, height + clearance],
        [top_width_offset - clearance, top_length_offset + length_top + clearance, height + clearance],

        // top - outer
        // TODO: With this solution, the angles of the walls are slightly
        //       changed. This is no problem at all, but not very "beautiful",
        //       because I know that it isn't perfect.
        [top_width_offset - clearance - plane_wall_thickness, top_length_offset - clearance - plane_wall_thickness, height + wall_thickness],
        [top_width_offset + width_top + clearance + plane_wall_thickness, top_length_offset - clearance - plane_wall_thickness, height + wall_thickness],
        [top_width_offset + width_top + clearance + plane_wall_thickness, top_length_offset + length_top + clearance + plane_wall_thickness, height + wall_thickness],
        [top_width_offset - clearance - plane_wall_thickness, top_length_offset + length_top + clearance + plane_wall_thickness, height + wall_thickness]
    ];
    
    faces = [
        [8, 9, 10, 11],   // top - inner

        [0, 8, 11, 3],    // left - inner
        [1, 2, 10, 9],    // right - inner

        [9, 8, 0, 1],     // front - inner
        [2, 3, 11, 10],   // back - inner

        [15, 14, 13, 12], // top - outer

        [7, 15, 12, 4],   // left - outer
        [13, 14, 6, 5],   // right - outer

        [5, 4, 12, 13],   // front - outer
        [14, 15, 7, 6],   // back - outer

        [0, 4, 5, 1],     // bottom - front
        [3, 2, 6, 7],     // bottom - back
        [0, 3, 7, 4],     // bottom - left
        [1, 5, 6, 2],     // bottom - right
    ];

    polyhedron(points, faces);
}


module _drone_part__contact_plate() {
    // Short versions of the variabled needed
    width = contact_plate_width;
    length = contact_plate_length;
    wall_thickness = contact_plate_wall_thickness;

    align_width_total = alignment_pin_width_base + 2*alignment_pin_slot_plane_wall_thickness;
    align_length_total = alignment_pin_length_base + 2*alignment_pin_slot_plane_wall_thickness;

    difference() {
        cube([width, length, wall_thickness]);

        // center cutout
        // TODO: Reduce in size. Only needs to be big enough to fit the locking
        //       mechanism of the container part.
        translate([alignment_pin_offset - alignment_pin_slot_plane_wall_thickness, align_length_total + 2*alignment_pin_offset, 0])
            cube([width - 2*(alignment_pin_offset - alignment_pin_slot_plane_wall_thickness),
                  length - 4*alignment_pin_offset - 2 * (align_length_total),
                  wall_thickness]);
        
        // cutout: alignment pin slot - front
        translate([alignment_pin_offset - 0.5*alignment_pin_clearance, alignment_pin_offset - 0.5*alignment_pin_clearance, 0])
            cube([alignment_pin_width_base + alignment_pin_clearance, alignment_pin_length_base + alignment_pin_clearance, wall_thickness]);
        
        // cutout: alignment pin slot - back
        translate([alignment_pin_offset - 0.5*alignment_pin_clearance, length - (alignment_pin_length_base + alignment_pin_clearance) - alignment_pin_offset + 0.5*alignment_pin_clearance, 0])
            cube([alignment_pin_width_base + alignment_pin_clearance, alignment_pin_length_base + alignment_pin_clearance, wall_thickness]);
    }
}


module drone_part() {
    union() {
        _drone_part__contact_plate();

        translate([alignment_pin_offset, alignment_pin_offset, 0])
            _drone_part__alignment_pin_slot();
        translate([alignment_pin_offset, contact_plate_length - alignment_pin_length_base - alignment_pin_offset, 0])
            _drone_part__alignment_pin_slot();
    }
}


// When executing the `export.sh` script, this variable will autimatically be
// set to true. The default value should be false.
export = false;
if(export) {
    drone_part();
}
