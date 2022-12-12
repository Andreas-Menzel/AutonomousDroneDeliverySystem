# 03 - Semi-automatic freight pick-up and drop-off

**Status:** work in progress

**Main Goal:** Create a mechanism that can securely attach a cargo container to
the drone and safely release it.

After compelting this milestone, the drone should have a "cargo area" and a
mechanism to securely attach a cargo container to it. It is ok if the drone and
the cargo container have to be precisely positioned (+- 5mm in each direction).
The mechanism should allow for a mid-flight drop-off.

The system can be an Arduino controlled prototype. The Arduino may be removed
and the mechanism may be controlled via the Raspberry Pi or the flight
controller later.

**Requirements**

- Lightweight mechanism
- Reliable mechanism
    - Don't wear off (fast) / Don't break
    - Allow for slightly misaligned cargo container
    - Allow for mid-flight drop-off without the cargo container getting caught
      on the drone

**Where you can find which files**

In this directory you can find images and 3d-files of the various prototypes
with information on advantages and disadvantages. The latest and currently used
version can be found in `/Cargo Holder/`.
