from NeuroLocoMiddleware.SoftRealtimeLoop import SoftRealtimeLoop
import time
import math
from TMotorCANControl.mit_can import TMotorManager_mit_can

# CHANGE THESE TO MATCH YOUR DEVICE!
Type = 'AK80-64'
ID = 1


def torque_step(dev):
    dev.set_zero_position()
    time.sleep(1.5) # wait for the motor to zero (~1 second)
    dev.set_current_gains()
    
    print("Starting torque step demo. Press ctrl+C to quit.")
    # loop = SoftRealtimeLoop(dt = 0.01, report=True, fade=0)
    for i in range(1000):
        dev.update()
        # if t < 1.0:
        
        dev.torque = 10.0
        # else:
        
            # dev.torque = 1.0
        
        print(math.degrees(dev.get_output_angle_radians())) 

        
    # del loop


if __name__ == '__main__':
    with TMotorManager_mit_can(motor_type=Type, motor_ID=ID) as dev:
        torque_step(dev)
