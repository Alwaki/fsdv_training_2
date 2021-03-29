# Task 2 - Introduction and running code
This repository contains the files for the second task in normal ROS package order. An additional report is included below in this README, answering some specified questions concerning the task.

To use the module, download it and run the launch file from within the package launch folder. This can be run using the command:

`roslaunch localization.launch`.

Furthermore, this module depends on the ROS package robot-localization. This package does not come with the default desktop ROS installation, and as such must be added separately. 

# Report
### What can happen if 1 measurement is delayed ?

If a measurement is delayed, this can propagate through the filter and result in a greater covariance (uncertainty) of the estimation of position. It depends how much redundancy is in the sensor update rate. For example, the GNSS updates at a much slower rate than the other sensors. As such, missing a satellite position input would have a greater effect than missing one sensor input from the wheel encoder.

### Now your IMU gets damaged. Does your implementation deal with it? How could you handle it?

If the IMU sensor becomes damaged, the implementation will still continue to run. There is no specific failsafe implemented, however alternative sensors will still work. A result will instead become fewer sensor inputs to fuse for the filters. A failsafe implementation could be implemented in the form of detecting no measurements coming from the IMU, and then injecting the system with a greater covariance to compensate for the added measurement uncertainty, essentially compensating for the fact that the system now is running with fewer sensors. Either that, or adding an additional IMU sensor for redundancy.

### Question 1: Which category is the most important in the Business Plan Presentation?

### Question 2: The driver must be able to leave the car quickly in an emergency. What does the regulations state about driver egress time?

### Question 3: Is it okay to adjust the angle of the winglets after technical inspection?

### Question 4: How many lateral g's are simulated during the tilt test?

### Question 5: How should the DV log data during the race?

### Question 6: What level of wireless communication with the vehicle (exclusing Remote Emergency System) is allowed during the race?
