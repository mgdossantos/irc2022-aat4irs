#!/usr/bin/env python3

from gazebo_msgs.srv import GetModelState
import rospy
import time
import os.path

class ListeningBox:
    def __init__(self):

        rospy.init_node('get_box_position')
        g_get_state = rospy.ServiceProxy("/gazebo/get_model_state", GetModelState)
        rospy.wait_for_service("/gazebo/get_model_state")
        try:
            self.state = g_get_state(model_name="red_box")
        except Exception as e:
            rospy.logerr('Error on calling service: %s', str(e))
            return

        # print(str(self.state.pose.position.x))
        self.x = self.state.pose.position.x


if __name__ == '__main__':

    if (os.path.isfile("/home/mdossantos/catkin_workspace/src/caseStudy2/tests/steps_defs/boxPositionX.txt")):
        f = open("/home/mdossantos/catkin_workspace/src/caseStudy2/tests/steps_defs/boxPositionX.txt", "a")
    else:
        f = open("/home/mdossantos/catkin_workspace/src/caseStudy2/tests/steps_defs/boxPositionX.txt", "x")


    try:
        box = ListeningBox()
    except rospy.ROSInterruptException:
        pass

    f.write(str(box.x)+"\n")
    f.close()
    time.sleep(2)
