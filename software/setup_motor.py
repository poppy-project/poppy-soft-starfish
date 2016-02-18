#!/usr/bin/env python

import sys
import json
import time

from argvee import Application
from pypot.dynamixel import Dxl320IO


config_file = 'config.json'
with open(config_file) as f:
    robot_config = json.load(f)


app = Application()


@app.cmd
def motorconfig(motor_name):
    with Dxl320IO('/dev/ttyUSB0') as io:
        for id in range(1, 254):
            if io.ping(id):
                break
        else:
            print(('No motor found on the bus! '
                   'Please make sure you have connected one and only motor.'))
            sys.exit(1)

        if not configure_motor(io, id, motor_name):
            print(('Something went wrong with the motor configuration. '
                   'You may retry a few times...'
                   'If the problem persists, check if no wire is unplugged or with another motor'))
            sys.exit(1)


def configure_motor(io, old_id, name):
    print('Starting to configure the motor...')
    motor_conf = robot_config['motors'][name]

    new_id = motor_conf['id']
    limits = motor_conf['angle_limit']

    # We cannot write to the EEPROM unless the torque is diabled.
    io.disable_torque([old_id])
    time.sleep(.5)

    if old_id != new_id:
        print('Changing the id...')
        io.change_id({old_id: new_id})
        time.sleep(.5)
        if not io.ping(new_id):
            return False

    print('Changing angle limit...')
    io.set_angle_limit({new_id: limits})
    time.sleep(.5)

    print('Adjusting return delay time...')
    io.set_return_delay_time({new_id: 0})
    time.sleep(.5)

    print('Your motor is now configured as:')
    print('Id: {}'.format(new_id))
    print('Angle Limit: {}'.format(limits))

    print('Going to Zero Position so it\'s ready to assemble...')
    io.set_moving_speed({new_id: 50})
    io.set_goal_position({new_id: 0})
    time.sleep(1.)
    print('Done!')

    io.disable_torque([new_id])

    return True


app.run()
