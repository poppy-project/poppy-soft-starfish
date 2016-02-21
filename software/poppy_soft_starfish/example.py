import pypot.robot

def init(robot):
    robot.power_up()
    for m in robot.motors:
        m.moving_speed = 50

def flatten(robot):
    init_pos = dict([(m.name, 0.0) for m in robot.motors])
    robot.goto_position(init_pos, 3., wait=True)

def move_arm(motor_group, m1_pos, m2_pos, duration=22, wait=True):
    pos_dict = {}
    pos_dict[motor_group[0].name] = m1_pos
    pos_dict[motor_group[1].name] = m2_pos
    robot.goto_position(pos_dict, duration, wait=wait)

def move(robot, pos_list, duration=2, wait=True):
    pos_dict = dict([(robot.motors[i].name, pos_list[i]) for i in range(len(pos_list))])
    robot.goto_position(pos_dict, duration, wait=wait)

def forward(robot):
    move(robot, [0,0,0,0,90,0])
    move(robot, [0,0,0,0,90,-120])
    move(robot, [0,0,0,0,45,-120])
    move(robot, [0,0,0,0,-45,-90])
    move(robot, [0,0,0,0,-45,-45])
    move(robot, [0,-90,0,-90,0,0])
    move(robot, [45,90,45,90,0,0])
    move(robot, [0,0,0,0,0,0])


if __name__ == '__main__':
    
    robot = pypot.robot.from_json('configuration/poppy_soft_starfish.json')
    
    init(robot)
    flatten(robot)

    for _ in range(10):
	forward(robot)


