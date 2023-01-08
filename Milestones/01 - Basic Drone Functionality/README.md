# 01 - Basic Drone Functionality

**Status:** work in progress

**Main Goal:** Create a "finished" hardware- & software setup for a basic flying
drone.

After completing this milestone, the drone should be able to be controlled
manually (lift-off, simple flying manouvres, landing) at nice weather with no
wind or other difficulties.

The drone does **not** have to use GPS to hold the current position or fly
waypoint missions. Other autonomous manouvres like auto-lift-off or auto-landing
are not part of this milestone.

**To achieve the main goal, the following tasks have to be finished:**

1. Select software
    - ... for the drone's flight controller
    - ... for the Ground Control Station (GCS)
2. Select & buy hardware
    - Basic drone hardware (frame, motors, ESCs, battery, transmitter &
      receiver, ...)
    - Flight controller
3. Build drone
    - Build hardware
    - Flash firmware to flight controller
    - Install and setup GCS software
4. Setup telemetry link between the drone and the GCS
5. Tune drone
    - Tune PID values of the flight controller
    - Optimize antenna positions at the ground station and on the drone

## 1. Select software

***TODO***

**ArduPilot** vs Betaflight vs ...

## 2. Select & buy hardware

### Preamble

There are two main approaches to getting the drone hardware for this project.

1. Buy a pre-built, well tuned drone, or
2. choose the individual components and build a "DIY-drone".

A list of advantages and disadvantages for using a DJI drone vs. a DIY drone can
be found in *DJI vs DIY.md*.

Option 1 has the advantage of having a well tuned drone that should be able to
fly simple (and advanced) manouvers out of the box. There are many different
models to choose from, e.g. the DJI Phantom 4 Pro V2 (, DJI Inspire 2, ...).

When choosing option 2, the drone can often be more easily modified and
extended. The price of a DIY-drone is also often (much) less, which is great;
especially for projects like this (student project with little budget).
Establishing a link between the drone and an external (but onboard) computer
can be easier when building the drone from scratch and choosing a suitable
flight controller. This is especially important in this project, because in the
end, the drone should be able to automatically start a mission when a
cargo-transport-mission is booked via an online service.

To simplify the process of connecting the drone to the on-board computer, to
money and to make this project more easily modifiable, I decided upon option 2,
the DIY-drone.

I am currently in the process of deciding which option to choose. When using
the pre-built version, the DJI Phantom 4 Pro V2 would be the drone of choice.
The ramainder of this README file will cover the DIY-version, since there is
more to be decided on.

Depending on the drone's requirements - in this project mainly payload and
stability - there are many different hardware components from which one
could choose. I already bought some drone hardware for a previous project I
didn't start (yet). (Re)using the hardware I already have, reduces the total
cost of this project. Since the hardware should pretty much result in a drone
according to this project's requirements, this would be the way to go.

### Choosing the drone's hardware

As we are using ArduPilot as our autopilot software, we can choose one of many
flight controllers, that can run ArduPilot. There are many different options,
ranging from basic ones (low-cost, few redundancy, ...) to high-end ones
(more expensive, redundant sensors, internal vibration dampening, ...).

**Frame:** Carbon fiber quadcopter frame ("WTOTOY")

- Price: ?€
- Size: ~ 47cm (width) x 43cm (length) from motor to motor
- Ground clearance: ~ 19cm

**Motors:** 4x "EMAX MT2216-810KV"

- Price: ~ 28€ (x4) - [buy here](https://emaxmodel.com/products/emax-multicopter-motor-mt2216-with-prop1045-combo)
- 2x CW-threaded
- 2x CCW-threaded

**Electronic Speed Controllers (ESC)**: 4x "EMAX BLHeli 30A"

- Price: ~ 20€ (x4) - [buy here](https://emaxmodel.com/products/blheli-series-30a-esc-oneshot-available?_pos=1&_sid=d06e995d7&_ss=r#)

**Propellers:** 4x (+ spare) 1045 nylon propellers

- Price: ~ 1€ (x2) - [buy here](https://emaxmodel.com/products/1045-nylon-propeller-cw-ccw-for-rc-quadcopter-for-emax-mt2213-mt2216-motors1-pair?variant=35882789830814#)
- 2x CW, 2x CCW
- Alternative: Premium propellers: 4x carbon fiber propellers
    - Price: ~ 9€ (x2) - [buy here](https://hobbyking.com/en_us/carbon-fiber-propeller-10x4-5-black-cw-2pcs.html)
    - 2x CW, 2x CCW

**Batteries:** 1x (+ spare) "Turnigy Multistar High Capacity 4S 5200mAh LiPo"
- Price: ~ ?€

**Flight Controller:** "Qio-Tek Zealot H743"
- Price: ~ 189€ - [buy here](https://smartfleet.systems/product/zealot-h743/)

**Telemetry Link:** "SiK Telemetry Radio V3"
- Price: ~ 54€ - [buy here](https://shop.holybro.com/sik-telemetry-radio-v3_p1103.html)

**PROS**

- Qio-Tek Zealot H743
    - Many sensors built-in with multiple redundancy
        - 3x gyroscope + accelerometer
        - 2x barometer
        - 1x compass
    - Internally vibration dampened
    - Temperature-controlled IMUs
    - Integrated AT7456E OSD chip
    - Sturdy aluminium case
- SiK Telemetry Radio V3
    - Can have good range. Especially better than WiFi.
