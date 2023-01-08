# DJI vs. DIY

Here is a list of advantages and disadvantages for using a DJI drone
(probably the *DJI Phantom 4 Pro V2*) vs. a DIY drone.

The components of the DIY drone can be found in the main README.md. The DIY
drone is (except for the flight controller & setup) finished.

## DJI Drone

### Pros

1. Pre-built and well functioning:
    - Very stable flight behaviour
    - Battery management
    - Good quality, aerodynamic design (without cargo)
    - ...
2. Easier position estimation: camera always points down thanks to the gimbal

### Cons

1. System not usable in production
    - Fundamental drone control is done on the ground
    - Drone must always be connected to the RC-transceiver
    - A separate phone is needed for each drone
2. No good place for the cargo (requirement: 300g - 500g cargo)
    - Cargo blocks the down-facing sensors & camera
    - Camera+gimbal are relatively big at the drone's center
    - Separate battery and receiver for cargo-lock
3. App development
    - More overhead
        - What happens when the phone is locked?
    - No (easy) access to the phone while in use
        - "On-the-field changes" complicated
        - Log-messages
4. My skills
    - I have never done anything with app-development
    - I am way more proficient in Python than Java

## DIY Drone

### Pros

1. System usable in production *(see con-1 for DJI drone)*
2. More reliable
    - Drone controls itself: can automatically fly on one-way path when
      connection to ground is lost
    - Less overhead (Android OS, locked phone, ...)
3. Modular build *(see con-2 for DJI drone)*
    - Easy to add new components (Raspberry Pi, Transceiver, ...)
    - Built specifically as a cargo-drone: no sensors are blocked
4. Debugging and "on-the-field changes" are easier
5. My skills
    - Mostly Python programming

### Cons

1. Initial setup
    - Build drone (mostly done)
    - Setup stable waypoint missions
2. Position estimation more difficult: Concider tilted drone
