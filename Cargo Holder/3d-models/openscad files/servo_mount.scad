//------------------------------------------------------------------------------
// Cargo holder - servo mount
//
// This model contains the mount of the servo which will be glued to the drone
// part.
//
// This model is part of the AutonomousDroneDeliverySystem:
// https://github.com/Andreas-Menzel/AutonomousDroneDeliverySystem
//------------------------------------------------------------------------------
// @author: Andreas Menzel
// @copyright: Copyright (c) 2022 Andreas Menzel
//------------------------------------------------------------------------------


include <dimensions.scad>


module _servo_mount__servo() {
    // Short versions of the variables needed
    wall_thickness = servo_slot_wall_thickness;
    height = servo_slot_height;
    mount_width = servo_mount_width;
    mount_thickness = servo_mount_thickness;
    mount_screw_slot_width = servo_mount_screw_slot_width;
    width = servo_body_width;
    length = servo_body_length;
    center_offset = servo_center_offset;
    height_offset = servo_height_offset;

    cp_width = contact_plate_width;
    cp_length = contact_plate_length;
    pin_diameter = locking_mechanism_pin_diameter;
    pin_clearance_key = locking_mechanism_pin_clearance_key;
    key_pin_outline = locking_mechanism_key_pin_outline;

    translate([0,
           (cp_length / 2) - ((length + 2*wall_thickness) / 2) + center_offset,
           ((pin_diameter + pin_clearance_key + 2*key_pin_outline) / 2) + height_offset]) union() {
        // Servo slot
        difference() {
            cube([width + wall_thickness, length + 2*wall_thickness, height]);
            
            translate([wall_thickness, wall_thickness, 0])
                cube([width, length, height]);
        }

        // Servo mounts
        difference() {
            union() {
                translate([0, -mount_width, 0])
                    cube([width + wall_thickness, mount_width, mount_thickness]);
                translate([0, length + 2*wall_thickness, 0])
                    cube([width + wall_thickness, mount_width, mount_thickness]);
            }
            
            // Screw slots
            translate([wall_thickness + (width / 2), -mount_width, 0])
                cube([mount_screw_slot_width,
                      2*mount_width + length + 2*wall_thickness,
                      mount_thickness]);
        }

    }
}

module _servo_mount__assembly() {
    // Short versions of the variables needed
    cp_width = contact_plate_width;
    length = servo_body_length;
    wall_thickness = servo_slot_wall_thickness;
    mount_width = servo_mount_width;
    center_offset = servo_center_offset;
    width = servo_body_width;
    assembly_thickness = servo_assembly_thickness;

    // Assembly (to mount the "servo mound" to the "drone part")
    inner_space = cp_width - 2*alignment_pin_offset - alignment_pin_length_top - (alignment_pin_length_base - alignment_pin_length_top) - (length + 2*wall_thickness + 2*mount_width);
    space_front = (inner_space / 2) + center_offset;
    space_back = (inner_space / 2) - center_offset;

    translate([0,
               alignment_pin_offset + ((alignment_pin_length_base - alignment_pin_length_top) / 2) + (alignment_pin_length_top / 2),
               alignment_pin_height + alignment_pin_slot_wall_thickness]) {

        cube([width + wall_thickness, space_front, assembly_thickness]);

        translate([0, space_front + (length + 2*wall_thickness + 2*mount_width), 0])
            cube([width + wall_thickness, space_back, assembly_thickness]);
    }
}


module servo_mount() {
    _servo_mount__servo();
    _servo_mount__assembly();
}


// When executing the `export.sh` script, this variable will autimatically be
// set to true. The default value should be false.
export = false;
if(export) {
    servo_mount();
}
