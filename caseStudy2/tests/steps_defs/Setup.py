import pytest
from pytest_bdd import scenarios, given, when, then
import time
import pyautogui
import rospy
import os

from kortex_driver.srv import *
from kortex_driver.msg import *


def setupRobot(typeRobot):
    if typeRobot == 1:
        pyautogui.hotkey('ctrl', 'alt', 't')
        time.sleep(2)
        pyautogui.write('roslaunch caseStudy2 spawn_kortex_robot.launch')
        pyautogui.press('enter')
        time.sleep(17)

def setupConveyor (typeConveyor):
    if typeConveyor == 1:
        pyautogui.hotkey('ctrl', 'alt', 't')
        time.sleep(2)
        pyautogui.write('rosrun  caseStudy2 box.py')
        pyautogui.press('enter')
        time.sleep(2)

def finalizeSystem(typeSystem):
    if typeSystem==1:
        pyautogui.hotkey('ctrl', 'shift', 'q')
        pyautogui.hotkey('ctrl', 'shift', 'q')
        pyautogui.press('enter')
        pyautogui.hotkey('ctrl', 'c')
        pyautogui.hotkey('ctrl', 'shift', 'q')
        pyautogui.press('enter')
        time.sleep(35)

    if typeSystem==2:
        pyautogui.hotkey('ctrl', 'shift', 'q')
        pyautogui.hotkey('ctrl', 'shift', 'q')
        pyautogui.hotkey('ctrl', 'c')
        time.sleep(35)
        pyautogui.hotkey('ctrl', 'shift', 'q')





