//------------------------------------------------------------------------------
// Cargo holder - assembled
//
// This model shows the complete, assembled mechanism. This model is not
// intended to be printed; it only functions as a visualisation.
//
// This model is part of the AutonomousDroneDeliverySystem:
// https://github.com/Andreas-Menzel/AutonomousDroneDeliverySystem
//------------------------------------------------------------------------------
// @author: Andreas Menzel
// @copyright: Copyright (c) 2022 Andreas Menzel
//------------------------------------------------------------------------------

include <dimensions.scad>
include <container_part.scad>
include <drone_part.scad>
include <locking_pin.scad>
include <servo_mount.scad>


cut = false;
vertical_gap = 150;

difference() {
    union() {
        container_part();

        translate([0, 0, contact_plate_wall_thickness + vertical_gap]) {
            drone_part();

            translate([(contact_plate_width / 2) - servo_slot_wall_thickness - (servo_body_width / 2),
                       0,
                       0])
                servo_mount();
        }
    }

    // Cut model in half, so that one can see that everything fits.
    if(cut) {
        translate([0, 70, 0])
            cube([1000, 1000, 1000]);
    }
}

//translate([-100, 0, 0]) locking_pin();