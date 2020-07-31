---
layout: post
title: Components under consideration for long-range, accurate autonomous missions
categories: emily, hardware
---

## Overview

Now that the vehicle is [controlling quite nicely after tuning](https://ekrell.github.io/PID-tuning-EMILY/), I am turning my attention to the long-range missions that we have in mind. Currently, the boat’s RF range is ~200 ft with a pair of [SiK Telemetry Radios](https://ardupilot.org/copter/docs/common-sik-telemetry-radio.html). Initially, we are interested in missions in Corpus Christi Bay, Oso Bay, Sunset Lake, the Laguna Madre, and the many other bodies of water in the Coastal Bend. Increasing communication range is of primary concern. 

While not as immediately critical, high accuracy GPS would allow us to produce more useful data products as well as improve navigation. I am especially interested in direct georeferencing so that data can be directly used to drive mission planning while onboard.

This post compiles some hardware components that are available for purchase that we are considering as well as links to related resources. 

#### Long-range RF telemetry: [RFD900 Radio Modem](https://ardupilot.org/copter/docs/common-rfd900.html#common-rfd900)

This RF pair is quite commonly used in ardu and PX4-based vehicles for longer range. It has a dedicated page in the [ArduPilot documentation](https://ardupilot.org/copter/docs/common-rfd900.html#common-rfd900). In fact, the EMILY was initially equipped with this when she was lent to us from [CRASAR](crasar.org). However, they needed their long-range radio back and we never actually tested them ourselves. I should get in contact and see if they still recommend this module. It is available from [JDrones for 280 USD](http://store.jdrones.com/jD_RD900Plus_Telemetry_Bundle_p/rf900set02.htm). 

Browsing the ArduBoat discussion forum, this telemetry solution is frequently recommended and appears in many of the boat builds. It is recommended [here](https://discuss.ardupilot.org/t/hi-power-radio-link/13891/2?u=ekrell1), [here](https://discuss.ardupilot.org/t/bait-boat-gps-system/13967/4?u=ekrell1), and is described [here as giving “much better range”](https://discuss.ardupilot.org/t/rugged-arduboat-for-mapping-applications-continued/9744/14?u=ekrell1). 

David Boulanger specifically [discusses](https://discuss.ardupilot.org/t/sailboat-support/32060/129?u=ekrell1) the range limitations of the SiK radios. The range is much less with a boat than when using the same telemetry on a rover or aerial vehicle. From a brief read of the thread, switching to RFD900 achieved acceptable range. Though, he also has a video where [UAVcast cellular telemetry](https://ardupilot.org/copter/docs/common-uavcast-telemetry.html) was used. 

Things to be aware of: 

- Recommended to power the RFD900 externally
- Need to adjust some parameters to use (not sure if to use _period_ or just to get better performance)

#### Cellular Telemetry

I have only recently started investigating this direction. Ultimately, it sounds like the way to go for truly long-range missions. I have never had issues with cellular reception while out fishing in the Laguna Madre. The infrastructure to support it looks substantially more involved, so I think it would be good to have the RFD900 for backup and for general testing. For now, I will just provide some options that I need to explore further. Before we decide on anything, we should consult [Conrad Blucher Institute](cbi.tamucc.edu), where I am told they have experience using cellular communication for their vehicles. Maybe, more specifically, the [MANTIS lab](https://mantisresearch.org/)?

[SPL Global Telemetry](http://envirover.com/docs/spl.html). Satellite and/or cellular system specifically intended for autonomous vehicles that use ArduPilot or PX4. Using it for control is integrated already into the ground control software [Mission Planner](https://ardupilot.org/planner/) and [QgroundControl](http://qgroundcontrol.com/). Using the cellular-only route requires a modem and plan as well as as Amazon Web Services account. I don’t think we need to go as extreme as satellite, which is significantly more expensive and requires even more hardware. Maybe once we master inshore autonomy, we can expand into the Gulf Coast. Here is an [ArduPilot forum post](https://discuss.ardupilot.org/t/stretching-comm-links-from-indoors-to-the-globe/45896). 

[UAVcast Cellular Telemetry](https://ardupilot.org/copter/docs/common-uavcast-telemetry.html). It is designed for MAVLink telemetry over 3G or 4G. I only came across this today, when I saw [David Boulanger using it](https://ardupilot.org/copter/docs/common-uavcast-telemetry.html) for his ArduPilot boat. He said that in open water he has been using it without issues. However, the video shows a scenario where the boat must go under a dock where it loses connection. The mission is saved by switching out the UAVcast with RFD900 at the base station since both were installed and operating on the boat. Redundancy is ideal. 

#### RTK GPS: u-blox ZED-F9P

U-blox products are ubiquitous when working with ArduPilot/PX4 vehicles. Most kits that I have seen come with a basic u-blox GPS/Compass like what we are currently using, U-blox Micro M8N GPS Compass module, that came with the [Pixhawk Mini](https://docs.px4.io/v1.9.0/en/flight_controller/pixhawk_mini.html). 

[U-blox ZED-F9P](https://www.u-blox.com/sites/default/files/ZED-F9P_ProductSummary_%28UBX-17005151%29.pdf) is a GPS module that can be used on the vehicle and at the base station. At base station, it is used to send corrections to the vehicle. [Wikipedia](https://en.wikipedia.org/wiki/Real-time_kinematic) has an overview of real-time kinematic (RTK) positioning, where a highly accurate base station fix is used to correct the vehicle’s less accurate readings in real time. Typically, this may provide centimeter-level accuracy. This module is released in several forms, including the [C099-F9P application board](https://www.u-blox.com/en/product/c099-f9p-application-board) (249 USD 
) and the [SparkFun GPS-RTK2 Board](https://www.sparkfun.com/products/15136) (220 USD). Roby at [deepsouthrobotics.com](deepsouthrobotics.com) gives a very detailed account of setting up a pair of  C099-F9P application boards for controlling an ArduRover vehicle with Mission Planner. And it looks like it is supported in [QgroundControl](https://docs.px4.io/master/en/gps_compass/rtk_gps.html) as well. 

