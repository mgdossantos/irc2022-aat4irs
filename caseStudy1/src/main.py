#!/usr/bin/env python3
import sys
import time
from kortex_driver.srv import *
from kortex_driver.msg import *
import pyautogui

from Setup import setupRobot, setupConveyor, finalizeSystem

from automatedMission import runExperiment

numberSimulations = 6

if __name__ == "__main__":

    count = 0
    while count < numberSimulations:
        setupRobot(1)
        setupConveyor(1)
        runExperiment()
        finalizeSystem(2)
        count = count + 1
        time.sleep(15)
