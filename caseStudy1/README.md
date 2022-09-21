# Case Study 1 - Without the Proposed Approach

# Requirements

* ROS
* gazebo
* ros-kortex

You can access a guideline for this installations (https://docs.google.com/presentation/d/1P1K28ihcsm6FGJCooZQ1cktJAYDkpnXx6-GcI8w_n1M/edit?usp=sharing)

# How to setup the tools

* Go to catkin_workspace/src
* Execute the command source /devel/setup.bash
* Create a package using catkin_create_pkg caseStudy1 rospy
* Download or clone the repository caseStudy1
* Copy all the sub-folder from folder caseStudy1/assests/models to your gazebo/models folder
* Copy the files on launch to ros_kortex/kortex_gazebo/launch/
* Copy the folder worlds on this repository to ros_kortex/kortex_gazebo
* Go to catkin_workspace/src and run the command catkin_make 

# How to run the experiments

* Open a terminal and run ` roslaunch caseStudy1 spawn_kortex_robot.launch`
* Open a terminal and run ` rosrun caseStudy1 box.py `
* Open another terminal and run ` rosrun caseStudy1 mission.py`


[![Watch the video] https://youtu.be/J_Z30YM9zlk
