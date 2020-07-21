---
layout: post
title: Autonomous waypoint following EMILY field test
categories: emily, field, laguna madre, autopilot
---
![Laguna Madre test site](../images/20200627_1.JPG)

### Overview

This morning, I took the EMILY out for another test in the Laguna Madre (27°38’28.5”N 97°12’09.7”W). This is the exact same launch point as Monday’s test, but now I am testing automatic control. The autopilot is a [Pixhawk Mini](https://docs.px4.io/v1.9.0/en/flight_controller/pixhawk_mini.html) running [ArduRover](https://ardupilot.org/rover/) firmware in boat mode. This is sometimes called [ArduBoat](https://discuss.ardupilot.org/c/ardurover/arduboat). 

The autopilot worked right away. It was able to head toward a waypoint as well as perform a return to launch (RTL) when requested. However, I need to do some parameter tuning for better control. The EMILY does not turn as smoothly as, say, a typical rover. So rather than go straight toward a waypoint, it keeps overshooting and oscillating on its path.

[EMILY autopilot video](https://youtu.be/yPgwaBPV9Zg)

### Issues

I am still limited by the low communication range. At ~300 feet, I lose both RC control and RF to the ground control laptop. I have the RF dongle on a tripod, but the range is significantly less than the advertised ~300 meters. Typically, around ~280 feet, I hear `Error Failsafe 0x1` which indicates RC loss. It automatically switches to a _hold_ mode and drifts for a bit. After a few seconds, the GCS communication is lost. Potential fixes for GCS communication include using the lab’s taller tripod or buying the long-range radios. For the Spektrum RC, I am using the Satellite receiver. There is also the Futuba RC that comes with the EMILY, though I’m not sure it has the channels needed for Pixhawk. I expect it has sufficiently long range since it was intended for the EMILY. Once connection is lost, I have to manually retrieve the EMILY, at least until it is within range again. 

![Control](../images/20200627_2.JPG)

![Control](../images/20200627_3.JPG)
