
from pytest_bdd import scenarios, given, when, then
import time
import pyautogui
import rospy
import os
from kortex_driver.srv import *
from kortex_driver.msg import *
from Setup import *


scenarios('../features/caseStudy2.feature')
@given("the robot setup is initialized")
def setup_robot():
    setupRobot(1)
@given("the conveyor setup is initialized")
def setup_conveyor():
   setupConveyor(1)
@given("the robot is at home")
def robot_position_initial():
    time.sleep(2)
    pyautogui.write('rosrun caseStudy2 readingGazeboRobot.py')
    pyautogui.press('enter')
    time.sleep(5)
    with open('/home/mdossantos/catkin_workspace/src/caseStudy2/tests/steps_defs/armPositionX.txt',
              'r') as input_file:
        for line in input_file:
            pass
        text = line
    assert  round(abs(abs(0.5761017203330994) - abs((float(text)))),2) <= 0.01
@given("the box is in the point A")
def box_positionA():
    time.sleep(2)
    pyautogui.write('rosrun caseStudy2 readingGazeboBox.py')
    pyautogui.press('enter')
    time.sleep(5)
    with open('/home/mdossantos/catkin_workspace/src/caseStudy2/tests/steps_defs/boxPositionX.txt',
              'r') as input_file:
        for line in input_file:
            pass
        text = line
    assert  round(abs(abs(0.5500000541335124) - abs((float(text)))),2) <= 0.02
    pyautogui.hotkey('ctrl', 'shift', 'q')

@when("the pickAndPlace finish")
def pickplace_mission():
    pyautogui.hotkey('ctrl', 'alt', 't')
    time.sleep(2)
    pyautogui.write('rosrun caseStudy2 mission.py')
    pyautogui.press('enter')
    timeout = 35
    ini = time.time()
    now = time.time()

    while now - ini <= timeout:
        time.sleep(1)
        now = time.time()
@then("the box should be in the position B")
def box_positionB():
    pyautogui.hotkey('ctrl', 'alt', 't')
    time.sleep(2)
    pyautogui.write('rosrun caseStudy2 readingGazeboBoxFinal.py')
    pyautogui.press('enter')
    time.sleep(5)
    finalizeSystem(1)
    with open('/home/mdossantos/catkin_workspace/src/caseStudy2/'
              'tests/steps_defs/boxPositionXFinal.txt',
              'r') as input_file:
        for line in input_file:
            pass
        text = line
    assert round(abs(abs(-0.32389056830347945) - abs((float(text)))),2) <= 0.02
