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

1. Select & buy hardware
    - Basic drone hardware (frame, motors, ESCs, battery, transmitter &
      receiver, ...)
    - Flight controller
2. Select software
    - ... for the drone's flight controller
    - ... for the Ground Control Station (GCS)
3. Build drone
    - Build hardware
    - Flash firmware to flight controller
    - Install and setup GCS software
4. Setup telemetry link between the drone and the GCS
5. Tune drone
    - Tune PID values of the flight controller
    - Optimize antenna positions at the ground station and on the drone

## 1. Select & buy hardware

Pre-assembled drone vs. DIY version (pros & cons)...
*<span style="color: orange">More information / Better explanations coming soon.</span>*

I already have many components...
*<span style="color: orange">More information / Better explanations coming soon.</span>*

### Choosing the drone's sceleton and muscles

This motors, ESCs, frame, ... because ...
*<span style="color: orange">More information / Better explanations coming soon.</span>*

### Choosing the drone's brain

ArduPilot is compatible with many different flight controllers, e.g. ...
*<span style="color: orange">More information / Better explanations coming soon.</span>*

Here is a list of different configurations:

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
