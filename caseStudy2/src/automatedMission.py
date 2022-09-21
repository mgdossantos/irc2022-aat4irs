import pytest
from pytest_bdd import scenarios, given, when, then
import time
import pyautogui
import rospy
import os

from kortex_driver.srv import *
from kortex_driver.msg import *


def runExperiment():
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
