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

## 2. Select & buy hardware

There are two main approaches to getting the drone hardware for this project.

1. Buy a pre-built, well tuned drone, or
2. choose the individual components and build a "DIY-drone".

Option 1 has the advantage of having a well tuned drone that should be able to
fly simple (and advanced) manouvers out of the box. There are many different
models to choose from, e.g.
*<span style="color: orange">More information</span>*

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

Depending on the drone's requirements - in this project mainly payload and
stability - there are many different hardware components from which one
could choose. I already bought some drone hardware for a previous project I
didn't start (yet). (Re)using the hardware I already have, reduces the total
cost of this project. Since the hardware should pretty much result in a drone
according to this project's requirements, this is the way to go.

### Choosing the drone's base-hardware

As stated before, I already had some drone hardware. The following list contains
the drone's base-hardware, meaning everything that does not calculate or measure
something.

- **Frame:** Carbon fiber quadcopter frame ("WTOTOY")
    - Size: approx. 45cm from motor to motor
- **Prototyping frame:** DIY: aluminum tubes + 3D-printed parts
    - Size: approx. 39cm from motor to motor
    - Little bit heavier than the main frame
    - Sturdier than the main frame
- **Motors:** 4x "EMAX MT2216-810KV"
    - 2x CW-threaded
    - 2x CCW-threaded
- **Electronic Speed Controllers (ESC)**: 4x "EMAX BLHeli 30A"
- **Propellers:** 4x (+ spare) 1045 plastic propellers
    - Additionaly: 4x carbon fiber propellers
- **Batteries:** 1x (+ spare) "Turnigy Multistar High Capacity 4S 5200mAh LiPo"
    - These batteries are pretty heavy (approx. 400g) and may be changed to
      lighter ones

***TODO:*** Add images (and links)

### Choosing the drone's brain

As we are using ArduPilot as our autopilot software, we can choose one of many
flight controllers, that can run ArduPilot. There are many different options,
ranging from basic ones (low-cost, few redundancy, ...) to high-end ones
(more expensive, redundant sensors, internal vibration dampening, ...).

***TODO:*** Remove list, clearly show the selected hardware and explain why other hardware was not chosen.

#### Configuration 1

Currently top-choice: many sensors, "professional" hardware.

**Price:** approx. 323€ - 353€

- Flight controller (189€ + 15€ shipping): "Qio-Tek Zealot H743" - standard edition with
  "u-block M10 GPS" gps module
    - Dimensions & weight: 65mm x 42mm x 25mm - 65g
    - buy here: [https://smartfleet.systems/product/zealot-h743/](https://smartfleet.systems/product/zealot-h743/)
- Range finder (30€ - 60€): "TFmini Plus" or "TF-Luna"
    - buy here: [https://www.amazon.de/youyeetoo-Single-Point-Measurement-Distance-Industrial/dp/B0823N72V8/](https://www.amazon.de/youyeetoo-Single-Point-Measurement-Distance-Industrial/dp/B0823N72V8/)
    - buy here: [https://www.amazon.de/youyeetoo-Single-Point-Measurement-Distance-Industrial/dp/B088BBJ9SQ/](https://www.amazon.de/youyeetoo-Single-Point-Measurement-Distance-Industrial/dp/B088BBJ9SQ/)
- Telementry link (56€ + 30€ shipping): "SiK Telemetry Radio V3"
    - buy here: [https://shop.holybro.com/sik-telemetry-radio-v3_p1103.html](https://shop.holybro.com/sik-telemetry-radio-v3_p1103.html)
- 20x foam pads (3€; shipping included in telemetry module)
    - buy here: [https://shop.holybro.com/foam-pads-20pcs_p1168.html](https://shop.holybro.com/foam-pads-20pcs_p1168.html)

PROS

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

CONS

- Qio-Tek Zealot H743
    - (closed hardware)

#### Configuration 2

Good configuration: many tutorials and good support for flight controller.
(not complete)

**Price:**

- Flight controller: "PixHawk 4" - **sold out**
    - Dimensions & weight: 84mm x 44mm x 12mm - 15.8g
- GPS + Compass (47€ + 25€ shipping): "Holybro M8N GPS"

PROS

- PixHawk flight controllers are widely used; support should be great
- (open hardware)

CONS

- **sold out**

#### Configuration 3

Also an option. The flight controller was suggested by a user on the ArduPilot
forum:
[https://discuss.ardupilot.org/t/what-flight-controller-to-use-for-an-autonomous-cargo-pick-up-and-drop-off-drone/93981](https://discuss.ardupilot.org/t/what-flight-controller-to-use-for-an-autonomous-cargo-pick-up-and-drop-off-drone/93981)
(not complete)

**Price:** approx: 158€

- Flight controller (110€): "Matek H743-Wing"
    - Dimensions & weight: 54mm x 36mm x 13mm - 30g
    - buy here: [https://n-factory.de/F405-WING_1](https://n-factory.de/F405-WING_1)
- GPS + Compass (48€): "Matek GNSS & Kompass M10-5883"
    - buy here: [https://n-factory.de/Matek-GNSS-Kompass-M10-5883_1](https://n-factory.de/Matek-GNSS-Kompass-M10-5883_1)

PROS

- MicroSD card black-box
- integrated AT7456E OSD chip
- Air speed sensor (?)
- (external buzzer)

## 2. Select Software

### Drone Software (Flight Controller)

ArduPilot Copter because reliable, good forums, ...
*<span style="color: orange">More information / Better explanations coming soon.</span>*

### Ground Control Station Software

Mission Planner because "way to go", used by many people, ...
*<span style="color: orange">More information / Better explanations coming soon.</span>*
