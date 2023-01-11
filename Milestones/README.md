# Milestones

The development of this project is split up into multiple parts ('milestones').
Generally one milestone needs to be finished before starting the next one.
Some milestones can be worked on simultaneously, depending on the temperature
and weather.


## Overview

This list gives an overview of the defined milestones. A directory exists for
each milestone, containing more information about the goals and requirements, as
well as the problems & ideas and the thinking behind achieving the current
goals.

Keep in mind that the definitions of the milestones (main goal, tasks to
complete, ...) can and will change as long as the milestone is still labeled as
"work in progress".

### 01 - Get and Setup Drone Hardware

**Status:** work in progress

**Main goal:** Select a suitable drone and achieve manual control.

After completing this milestone, we should have a drone (pre-built or diy) that
we can manually control. Simple autonomous flight modes (automatic takeoff and
landing, waypoint missions) should also be possible.

### 02 - Basic Drone Control

**Status:** *pending*

**Main Goal:** Establish a connection between the drone and a self-written
script / program.

After completing this milestone, a self-written script / program should be able
to control the drone: Flying from side to side, auto takeoff / landing and
custom waypoint missions.

### 03 - Cargo Holder

**Status:** work in progress

**Main Goal:** Create a mechanism that can securely attach a cargo container to
the drone and safely release it.

After compelting this milestone, the drone should have a cargo area and a
mechanism to securely attach a cargo container to it. It is ok if the drone and
the cargo container have to be "precisely" positioned (+- 5mm in each direction).

### 04 - Cargo Station Detection and Positioning

**Status:** work in progress

**Main Goal:** Detect a Cargo Station and position the drone centered above.

After completing this milestone, the drone should be able to detect a Cargo
Station (e.g. via ArUco markers) and position itself directly above.

---

**To be updated:**

---

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

### optional? - 07 - Fully Autonomous Cargo Pick-Up and Drop-Off

**Status:** *pending*

**Main Goal:** Fully autonomously attach and detach a cargo container to / from
the drone.

After completing this milestone, the cargo station should have a mechanism that
either brings the cargo container to the drone, or vice versa. The cargo
container should then be fully autonomously attached / detached to / from the
drone after an autonomous landing.

### optional? - 08 - Fully Autonomous Pick-Up, Transport and Drop-Off Routine

**Status:** *pending*

**Main Goal:** Connect the autonomous pick-up, transport, landing and drop-off
sequences.

After completing this milestone, the drone should be able to fully autonomously
land, pick-up a cargo container, lift off, fly to the next cargo station, land
and drop the cargo container off.
