import pypot.robot


robot = pypot.robot.from_json('configuration/poppy_soft_starfish.json')

for m in robot.motors:
    m.compliant=Fals
    m.moving_speed = 50
