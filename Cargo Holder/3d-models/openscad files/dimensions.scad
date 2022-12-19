//------------------------------------------------------------------------------
// Cargo holder - dimensions
//
// This file contains the dimensions for the cargo holder mechanism.
//
// This model is part of the AutonomousDroneDeliverySystem:
// https://github.com/Andreas-Menzel/AutonomousDroneDeliverySystem
//------------------------------------------------------------------------------
// @author: Andreas Menzel
// @copyright: Copyright (c) 2022 Andreas Menzel
//------------------------------------------------------------------------------

// Notes:
// - width, length and height are always in relation to the drone, unless
//   explicitly stated otherwise

//////////////////////////////// Contact Plate /////////////////////////////////
// The contact plates of the container- and drone- part touch. They have the
// same size. TODO: Use magnets to help with the alignment of the parts?
contact_plate_width = 150;
contact_plate_length = 150;
contact_plate_wall_thickness = 2;

//////////////////////////////// Alignment Pin /////////////////////////////////
// Pins used to align the cargo container relative to the drone. This mechanism
// can (only) correct small misalignments.

// Offset from the contact plate sides
alignment_pin_offset = 5;
// Clearance (on all sides) to allow for slightly misaligned drone / cargo
// container
alignment_pin_align_clearance = 7;

alignment_pin_width_base = contact_plate_width - 2*alignment_pin_offset;
alignment_pin_length_base = 17;

alignment_pin_width_top = alignment_pin_width_base - 2*alignment_pin_align_clearance;
alignment_pin_length_top = alignment_pin_length_base - 2*alignment_pin_align_clearance;

alignment_pin_height = 20;

alignment_pin_slot_wall_thickness = 2;
// The wall thickness of the alignment pin slot measured in XY-plane. The
// The wall thickness is slightly smaller. TODO: calculate correctly.
alignment_pin_slot_plane_wall_thickness = 2.5;

// Half of the clearance will be added to each part (container / drone)
alignment_pin_clearance = 0.25;

// Center cutout of the alignment pin. For weight reduction.
alignment_pin_center_cutout_width = contact_plate_width - 2*alignment_pin_offset - (alignment_pin_width_base - alignment_pin_width_top) - 2*20;

////////////////////////////// Locking Mechanism ///////////////////////////////
locking_mechanism_pin_wire_diamter = 1;
locking_mechanism_pin_wire_connection_outline = 2;
locking_mechanism_pin_diameter = 10;
locking_mechanism_pin_clearance_lock = 0.5;
locking_mechanism_pin_clearance_key = 2;

locking_mechanism_lock_key_clearance = 2*alignment_pin_align_clearance;

// The key part is located on the container
locking_mechanism_key_thickness = 4;
locking_mechanism_key_pin_outline = 4; // Wall thickness around the hole of the
                                       // locking pin.

// The lock part is located on the drone
locking_mechanism_lock_offset = alignment_pin_offset;
locking_mechanism_lock_wall_thickness = 3;
locking_mechanism_lock_rest_length = locking_mechanism_lock_key_clearance + locking_mechanism_key_thickness;
locking_mechanism_lock_rest_wall_thickness = 2;

///////////////////////////////// Servo Mount //////////////////////////////////
servo_slot_wall_thickness = 2;
servo_slot_height = 10;

servo_mount_width = 5;
servo_mount_thickness = 7;
servo_mount_screw_slot_width = 0.75;

servo_assembly_thickness = 5;

// The width OF THE SERVO - smaller side of the servo; not in relation to the
// drone
servo_body_width = 12;
// The length OF THE SERVO - larger side of the servo; not in relation to the
// drone
servo_body_length = 23;
servo_center_offset = 6;
servo_height_offset = 11;

// Wall thickness of the slot on the drone part in which the servo mount will be
// glued to.
servo_mount_drone_part_wall_thickness = 3;
