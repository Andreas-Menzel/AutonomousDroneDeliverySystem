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
alignment_pin_offset = 10;

alignment_pin_width_base = contact_plate_width - 2*alignment_pin_offset;
alignment_pin_length_base = 25;

alignment_pin_width_top = alignment_pin_width_base - 20;
alignment_pin_length_top = alignment_pin_length_base - 20;

alignment_pin_height = 20;

alignment_pin_slot_wall_thickness = 2;
// The wall thickness of the alignment pin slot measured in XY-plane. The
// The wall thickness is slightly smaller. TODO: calculate correctly.
alignment_pin_slot_plane_wall_thickness = 2.5;

// Half of the clearance will be added to each part (container / drone)
alignment_pin_clearance = 0.25;
