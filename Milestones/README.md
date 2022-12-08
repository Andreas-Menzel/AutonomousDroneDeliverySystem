# Milestones

The development of this project is split up into multiple parts ('milestones').
Generally one milestone needs to be finished before starting the next one.


## Overview

This list gives an overview of the defined milestones. A directory exists for
each milestone, containing more information about the goals and requirements, as
well as the problems & ideas and the thinking behind achieving the current
goals.

Keep in mind that the definitions of the milestones (main goal, tasks to
complete, ...) can and will change as long as the milestone is still labeled as
"work in progress".

### 01 - Basic Drone Functionality

**Status:** work in progress

**Main Goal:** Create a "finished" hardware- & software setup for a basic flying
drone.

After completing this milestone, the drone should be able to be controlled
manually (lift-off, simple flying manouvres, landing) at nice weather with no
wind or other difficulties.

The drone does **not** have to use GPS to hold the current position or fly
waypoint missions. Other autonomous manouvres like auto-lift-off or auto-landing
are not part of this milestone.

### 02 - Basic Autonomous Flying

**Status:** *pending*

**Main Goal:** Incorporate GPS module and fly small autonomous missions.

After completing this milestone, the drone should be able to autonomously
take off, hold a gps-location, fly small missions (follow gps-route) and land.

The drone does **not** have to perform a precision landing.

### 03 - Semi-automatic freight pick-up and drop-off

**Status:** *pending*

**Main Goal:** Create a mechanism that can securely attach a cargo container to
the drone and safely release it.

After compelting this milestone, the drone should have a "cargo area" and a
mechanism to securely attach a cargo container to it. It is ok if the drone and
the cargo container have to be precisely positioned (+- 5mm in each direction).
The mechanism should allow a mid-flight drop-off.

The system can be an Arduino controlled prototype. The Arduino may be removed
and the mechanism may be controlled via the Raspberry Pi later.

---

**The system (drone + GCS) does now fulfill the basic cargo pick-up, transport**
**and drop-off requirements. The cargo container attachement- / release-**
**sequences, as well as the gps-waypoint missions, can be initiated manually.**

---

### 04 - Authentications and Verifications

**Status:** *pending*

**Goal:** Authentications and verifications of the drone, terminal and bookings
through C-Chain.

**The content of this milestone is still to be discussed.**

### optional? - Drone Control via Raspberry Pi

**Status:** *pending*

**Main Goal:** Establish a communication link between the flight controller and
the Raspberry Pi. Execute simple (flight) routines with the Raspberry Pi.

After completing this milestone, the Raspberry Pi should be able to send (basic)
commands to the flight controller (and read back the results). The drone should
be controlled, so that it ...

1. can be (dis-)armed,
2. lifts off,
3. flies left to right and
4. flies to a gps-location
