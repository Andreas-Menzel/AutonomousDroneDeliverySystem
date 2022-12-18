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

    length = 2*lock_wall_thickness + key_thickness + lock_key_clearance;

    wire_diameter = locking_mechanism_pin_wire_diamter;
    connection_outline = locking_mechanism_pin_wire_connection_outline;
    

    union() {
        // Main pin
        cylinder(d=pin_diameter, h=length);

        // Connector
        //cube([wire_diameter]);
    }
}


// When executing the `export.sh` script, this variable will autimatically be
// set to true. The default value should be false.
export = false;
if(export) {
    locking_pin();
}
