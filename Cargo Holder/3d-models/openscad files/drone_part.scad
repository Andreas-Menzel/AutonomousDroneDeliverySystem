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


module _drone_part__locking_mechanism_lock() {
    // Short versions of the variables needed
    wall_thickness = locking_mechanism_lock_wall_thickness;
    pin_diameter = locking_mechanism_pin_diameter;
    pin_clearance = locking_mechanism_pin_clearance_lock;
    pin_clearance_key = locking_mechanism_pin_clearance_key;

    rest_length = locking_mechanism_lock_rest_length;
    rest_wall_thickness = locking_mechanism_lock_rest_wall_thickness;

    lock_key_clearance = locking_mechanism_lock_key_clearance;
    key_thickness = locking_mechanism_key_thickness;

    key_pin_outline = locking_mechanism_key_pin_outline;

    width_without_rest = wall_thickness + wall_thickness + key_thickness + lock_key_clearance;
    length = pin_diameter + pin_clearance_key + lock_key_clearance + 2*wall_thickness + 2*key_pin_outline;
    height = pin_diameter + pin_clearance_key + wall_thickness + 2*key_pin_outline;

    // Lock
    difference() {
        union() {
            // Top
            translate([0, 0, height - wall_thickness])
                cube([width_without_rest,
                      length, wall_thickness]);
            // Left
            cube([wall_thickness, length, height]);
            // Right
            translate([wall_thickness + key_thickness + lock_key_clearance, 0, 0])
                cube([wall_thickness, length, height]);
            
            // Front
            cube([2*wall_thickness + key_thickness + lock_key_clearance,
                  wall_thickness, height]);
            // Back
            translate([0, length - wall_thickness, 0])
                cube([2*wall_thickness + key_thickness + lock_key_clearance,
                      wall_thickness, height]);
            
            // Wall - rest
            translate([2*wall_thickness + key_thickness + lock_key_clearance,
                       length / 2,
                       (height - wall_thickness) / 2]) {
                rotate([0, 90, 0])
                    cylinder(d=pin_diameter + pin_clearance + 2*rest_wall_thickness,
                            h=rest_length);
                
                translate([0,
                           -((pin_diameter + pin_clearance + 2*rest_wall_thickness) / 2),
                           -((pin_diameter + pin_clearance + 2*rest_wall_thickness) / 2)])
                    cube([rest_length,
                          pin_diameter + pin_clearance + 2*rest_wall_thickness,
                          (pin_diameter + pin_clearance + 2*rest_wall_thickness) / 2]);
            }
        }

        // Hole for the pin
        translate([0, length / 2, (height - wall_thickness) / 2])
            rotate([0, 90, 0])
            cylinder(d=pin_diameter + pin_clearance,
                     h=2*wall_thickness + key_thickness + lock_key_clearance + rest_length);
    }
}


module _drone_part__locking_mechanism() {
    // Short versions of the variables needed
    pin_diameter = locking_mechanism_pin_diameter;
    pin_clearance_key = locking_mechanism_pin_clearance_key;
    lock_key_clearance = locking_mechanism_lock_key_clearance;
    wall_thickness_lock = locking_mechanism_lock_wall_thickness;
    key_pin_outline = locking_mechanism_key_pin_outline;
    key_thickness = locking_mechanism_key_thickness;
    lock_offset = locking_mechanism_lock_offset;

    width_without_rest = 2*wall_thickness_lock + key_thickness + lock_key_clearance;
    length = pin_diameter + pin_clearance_key + lock_key_clearance + 2*wall_thickness_lock + 2*key_pin_outline;

    lock_distance_from_center = contact_plate_width / 2 - width_without_rest - lock_offset;

    translate([-(width_without_rest + lock_distance_from_center), 0, 0])
        _drone_part__locking_mechanism_lock();

    translate([width_without_rest + lock_distance_from_center, length, 0])
        rotate([0, 0, 180])
        _drone_part__locking_mechanism_lock();
}


module _drone_part__alignment_pin_slot() {
    // Short versions of the variables needed
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
    // Short versions of the variables needed
    width = contact_plate_width;
    length = contact_plate_length;
    wall_thickness = contact_plate_wall_thickness;

    pin_diameter = locking_mechanism_pin_diameter;
    pin_clearance_key = locking_mechanism_pin_clearance_key;
    lock_key_clearance = locking_mechanism_lock_key_clearance;
    wall_thickness_lock = locking_mechanism_lock_wall_thickness;
    key_pin_outline = locking_mechanism_key_pin_outline;
    key_thickness = locking_mechanism_key_thickness;

    align_width_total = alignment_pin_width_base + 2*alignment_pin_slot_plane_wall_thickness;
    align_length_total = alignment_pin_length_base + 2*alignment_pin_slot_plane_wall_thickness;

    lock_length = pin_diameter + pin_clearance_key + lock_key_clearance + 2*wall_thickness_lock + 2*key_pin_outline;

    difference() {
        cube([width, length, wall_thickness]);

        //cutout: lock - left
        translate([locking_mechanism_lock_offset + wall_thickness_lock,
                   contact_plate_length / 2 - lock_length / 2,
                   0])
            cube([lock_key_clearance + key_thickness, lock_length, wall_thickness]);

        //cutout: lock - right
        translate([contact_plate_width - (lock_key_clearance + key_thickness) - (locking_mechanism_lock_offset + wall_thickness_lock),
                   contact_plate_length / 2 - lock_length / 2,
                   0])
            cube([lock_key_clearance + key_thickness, lock_length, wall_thickness]);
        
        // cutout: alignment pin slot - front
        translate([alignment_pin_offset - 0.5*alignment_pin_clearance, alignment_pin_offset - 0.5*alignment_pin_clearance, 0])
            cube([alignment_pin_width_base + alignment_pin_clearance, alignment_pin_length_base + alignment_pin_clearance, wall_thickness]);
        
        // cutout: alignment pin slot - back
        translate([alignment_pin_offset - 0.5*alignment_pin_clearance, length - (alignment_pin_length_base + alignment_pin_clearance) - alignment_pin_offset + 0.5*alignment_pin_clearance, 0])
            cube([alignment_pin_width_base + alignment_pin_clearance, alignment_pin_length_base + alignment_pin_clearance, wall_thickness]);
    }
}


module drone_part__servo_mount_slot() {
    // Short versions of the variables needed
    slot_wall_thickness = servo_mount_drone_part_wall_thickness;

    slot_width = servo_body_width + servo_slot_wall_thickness;
    slot_length = alignment_pin_length_top / 2;
    slot_height = servo_assembly_thickness;

    difference() {
        translate([-slot_wall_thickness, -slot_wall_thickness, 0])
            cube([slot_width + 2*slot_wall_thickness,
                  slot_length + slot_wall_thickness,
                  slot_height]);
        
        cube([slot_width, slot_length, slot_height]);
    }
}

drone_part();
module drone_part() {
    // Short versions of the variables needed
    lm_pin_diameter = locking_mechanism_pin_diameter;
    lm_pin_clearance_key = locking_mechanism_pin_clearance_key;
    lm_lock_key_clearance = locking_mechanism_lock_key_clearance;
    lm_wall_thickness_lock = locking_mechanism_lock_wall_thickness;
    lm_key_pin_outline = locking_mechanism_key_pin_outline;

    lm_length = lm_pin_diameter + lm_pin_clearance_key + lm_lock_key_clearance + 2*lm_wall_thickness_lock + 2*lm_key_pin_outline;

    cp_width = contact_plate_width;

    union() {
        _drone_part__contact_plate();

        translate([alignment_pin_offset, alignment_pin_offset, 0])
            _drone_part__alignment_pin_slot();
        translate([alignment_pin_offset, contact_plate_length - alignment_pin_length_base - alignment_pin_offset, 0])
            _drone_part__alignment_pin_slot();
        
        translate([contact_plate_width / 2, (contact_plate_length / 2) - (lm_length / 2), 0])
            _drone_part__locking_mechanism();
        
        translate([(cp_width / 2) - (servo_body_width / 2) - servo_slot_wall_thickness,
                    0,
                    alignment_pin_height + alignment_pin_slot_wall_thickness]) {
            
            translate([0,
                       alignment_pin_offset + ((alignment_pin_length_base - alignment_pin_length_top) / 2) + (alignment_pin_length_top / 2),
                       0])
                drone_part__servo_mount_slot();
            
            translate([0,
                       cp_width - (alignment_pin_offset + ((alignment_pin_length_base - alignment_pin_length_top) / 2) + (alignment_pin_length_top / 2)),
                       0])
                translate([servo_body_width + servo_slot_wall_thickness, 0, 0])
                rotate([0, 0, 180])
                drone_part__servo_mount_slot();
        }
    }
}


// When executing the `export.sh` script, this variable will autimatically be
// set to true. The default value should be false.
export = false;
if(export) {
    drone_part();
}
