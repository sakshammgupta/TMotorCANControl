from NeuroLocoMiddleware.SoftRealtimeLoop import SoftRealtimeLoop
# try:
#      from TMotorCANControl.TMotorManager import TMotorManager
# except ModuleNotFoundError:
from sys import path
path.append("/home/pi/TMotorCANControl/src/")
import os
import sys
cur_path=os.path.abspath(os.path.dirname(__file__))
sys.path.insert(0, cur_path+"/../..")

from TMotorCANControl.servo_can import *
# from TMotorCANControl.servo_can import TMotorManager_servo_can
import time

with TMotorManager_servo_can(motor_type='AK80-64', motor_ID=1) as dev:
    
    loop = SoftRealtimeLoop(dt=0.005, report=True, fade=0.0)
    dev.enter_idle_mode()
    dev.set_zero_position()
    for t in loop:
        dev.update()
        print("\r" + str(dev),end='')