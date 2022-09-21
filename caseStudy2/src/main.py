#!/usr/bin/env python3
import sys
import time
from kortex_driver.srv import *
from kortex_driver.msg import *
import pyautogui

sys.path.append('/home/mdossantos/catkin_workspace/src/caseStudy2/tests/steps_defs')
from Setup import setupRobot, setupConveyor, finalizeSystem

from automatedMission import runExperiment

numberSimulations = 1

if __name__ == "__main__":

    count = 0
    while count < numberSimulations:
        setupRobot(1)
        setupConveyor(1)
        runExperiment()
        finalizeSystem(2)
        count = count + 1
