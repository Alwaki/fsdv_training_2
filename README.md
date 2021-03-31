# Task 2 - Introduction and running code
This repository contains the files for the second task in normal ROS package order. An additional report is included below in this README, answering some specified questions concerning the task.

To use the module, download it and run the launch file from within the package launch folder. This can be run using the command:

`roslaunch localization.launch`.

Furthermore, this module depends on the ROS package robot-localization. This package does not come with the default desktop ROS installation, and as such must be added separately. 

# Report
## Description
To solve this problem, I utilized the package robot_localization from the ROS framework. By using two separate EKF filters, I could integrate the sensor data in two steps. Initially, the sensor data from the speedometer and the IMU unit was fused in continuous time. Then the result of this fusion was again fused with the GPS data. As the GPS data was given in nav_msgs/Odometry form, the built in package for nav_sat integration could not be used. As such, this structure of two common EKF filters was used instead.

## Answers to Questions

### What can happen if 1 measurement is delayed ?

If a measurement is delayed, this can propagate through the filter and result in a greater covariance (uncertainty) of the estimation of position. It depends how much redundancy is in the sensor update rate. For example, the GNSS updates at a much slower rate than the other sensors. As such, missing a satellite position input would have a greater effect than missing one sensor input from the wheel encoder.

### Now your IMU gets damaged. Does your implementation deal with it? How could you handle it?

If the IMU sensor becomes damaged, the implementation will still continue to run. There is no specific failsafe implemented, however alternative sensors will still work. A result will instead become fewer sensor inputs to fuse for the filters. A failsafe implementation could be implemented in the form of detecting no measurements coming from the IMU, and then injecting the system with a greater covariance to compensate for the added measurement uncertainty, essentially compensating for the fact that the system now is running with fewer sensors. Either that, or adding an additional IMU sensor for redundancy.

### Which category is the most important in the Business Plan Presentation?
Content (20 pts)
### The driver must be able to leave the car quickly in an emergency. What does the regulations state about driver egress time?
Egress is considered complete when the driver stands next to the car both feet on the ground.
### Is it okay to adjust the angle of the winglets after technical inspection?
Yes
### How many lateral g's are simulated during the tilt test?
None of the above
### How should the DV log data during the race?
Teams must install the standardised data logger piece of hardware provided by the officials on their vehicle.
### What level of wireless communication with the vehicle (exclusing Remote Emergency System) is allowed during the race?
Only one-way-telemetry for information retrieval is allowed.
