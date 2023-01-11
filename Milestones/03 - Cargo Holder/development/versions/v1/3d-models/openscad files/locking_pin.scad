//------------------------------------------------------------------------------
// Cargo holder - locking pin
//
// This model contains the pin to lock the container to the drone.
//
// This model is part of the AutonomousDroneDeliverySystem:
// https://github.com/Andreas-Menzel/AutonomousDroneDeliverySystem
//------------------------------------------------------------------------------
// @author: Andreas Menzel
// @copyright: Copyright (c) 2022 Andreas Menzel
//------------------------------------------------------------------------------


include <dimensions.scad>


module locking_pin() {
    // Short versions of the variables needed
    pin_diameter = locking_mechanism_pin_diameter;
    lock_wall_thickness = locking_mechanism_lock_wall_thickness;
    key_thickness = locking_mechanism_key_thickness;
    lock_key_clearance = locking_mechanism_lock_key_clearance;
    rest_length = locking_mechanism_lock_rest_length;
    tip_length = locking_mechanism_pin_tip_length;
    tip_diameter = locking_mechanism_pin_tip_diameter;

    slide_length = 2*lock_wall_thickness + key_thickness + lock_key_clearance + rest_length;

    wire_diameter = locking_mechanism_pin_wire_diamter;
    connection_length = locking_mechanism_pin_connection_length;
    
$fn=30;
    difference() {
        // Main pin
        hull() {
            cylinder(d=pin_diameter, h=slide_length + connection_length - tip_length);
            translate([0, 0, slide_length + connection_length - (tip_diameter / 2)])
                sphere(d=tip_diameter);
        }

        translate([-pin_diameter / 2, 0, connection_length / 2])
            rotate([0, 90, 0])
            cylinder(d=wire_diameter, h=pin_diameter);
        translate([-pin_diameter / 2, 0, 0])
            rotate([0, 90, 0])
            cylinder(d=wire_diameter, h=pin_diameter);
        
        cylinder(d=pin_diameter / 2 ,h=wire_diameter);
    }
}


// When executing the `export.sh` script, this variable will autimatically be
// set to true. The default value should be false.
export = true;
if(export) {
    locking_pin();
}
