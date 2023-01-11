# Get and Setup Drone Hardware

**Status:** work in progress

**Main goal:** Select a suitable drone and achieve manual control.

After completing this milestone, we should have a drone (pre-built or diy) that
we can manually control. Simple autonomous flight modes (automatic takeoff and
landing, waypoint missions) should also be possible.

**To achieve the main goal, the following tasks have to be finished:**

1. Choose whether to use a pre-built drone (e.g. from DJI) or to build and
   setup an own drone system.
2. Select ground control software and software to control the drone through an
   own script / program.
3. Buy  drone and / or components (and assemble)

## 1. Select Drone: DIY or buy?

There are two main approaches to getting the drone hardware for this project.

1. Buy a pre-built, well tuned drone, or
2. Choose the individual components and build a "DIY-drone".

Option 1 has the advantage of having a well tuned drone that should be able to
fly simple (and advanced) manouvers out of the box. There are many different
models to choose from, e.g. the DJI Phantom 4 Pro V2 (, DJI Phyntom 4 RTK, ...).
When choosing option 2, the drone can often be more easily modified and
extended. Developing and tuning such a drone takes a lot of time, however.

Due to the time contraints of this project, option 1 - pre-built drone - is the
way to go. I will be using the **DJI Phantom 4 Pro V2**. It is a rather small,
but very capable and well tuned drone.

Since the DJI Phantom 4 Pro V2 was designed as a camera drone, there are a few
challenges to overcome. For example the placement, size and weight of the cargo
container.

After this project is finished I will definitely "start again" and
build a drone from scratch using ArduPilot as the flight controller software,
python scripts to control the drones behaviour and the knowledge I gained during
this project.

## 2. Select Software

DJI provides multiple SDKs to write own code to control the drone:

1. Mobile SDK
2. Onboard SDK
3. Windows SDK

The Mobile SDK runs as an App on an Android or iOS phone. The phone has to be
connected to the rc transciever via usb or wifi. This is the main disadvantage
of this method: The drone must always be connected to the remote. This is not
possible / viable when deploying a fleet of drones over a wide area. In this
project, which is intended as a proof of concept, it is ok.

The Onboard SDK runs directly on the drone. The rc remote is not required during
operation. The DJI Phantom 4 Pro V2 (and the RTK version) is not supported.

The Windows SDK is similar to the Mobile SDK: An app is created to control the
drone. This time the app runs on a Windows 10 device.

**It is still undecided whether I will use the Mobile SDK or the Windows SDK.**

## 3. Buy Drone Hardware

Thanks to *Prof. Dr.-Ing. Markus Ryll* and the
*TUM Department Aerospace and Geodesy* at the
*TUM School of Engineering and Design* I will be able to use multiple
Phantom 4 Pro V2 (or the RTK version) for testing and the final presentation.
Many thanks!
