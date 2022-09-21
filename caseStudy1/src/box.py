#!/usr/bin/env python3
import tf.transformations
from gazebo_msgs.srv import SpawnModel
import rospy
from geometry_msgs.msg import Pose, Quaternion, Point
import random


def main():
    rospy.init_node('red_box', log_level=rospy.INFO)
    rospy.wait_for_service("/gazebo/spawn_sdf_model")
    spawn_model_client = rospy.ServiceProxy('/gazebo/spawn_sdf_model', SpawnModel)
    orient = Quaternion(*tf.transformations.quaternion_from_euler(0, 0, 0))
    n = random.randint(0,22)
    if n%2==0 :
    	r = random.uniform(-0.025, 0.025)
    	position = Point(0.55+r, 0.2, 1)
    else:
    	position = Point(0.55, 0.2, 1)
    spawn_model_client(model_name='red_box',
                       model_xml=open('/home/mdossantos/.gazebo/models/red_box/model.sdf', 'r').read(),
                       robot_namespace='/red_box', initial_pose=Pose(position, orient), reference_frame='world')


if __name__ == '__main__':
    try:
        main()
    except rospy.ROSInterruptException:
        pass
