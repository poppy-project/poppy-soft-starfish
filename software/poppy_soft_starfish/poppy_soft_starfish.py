from numpy import sum
from functools import partial

from poppy.creatures import AbstractPoppyCreature


class PoppySoftStarfish(AbstractPoppyCreature):

    @classmethod
    def setup(cls, robot):
        robot._primitive_manager._filter = partial(sum, axis=0)

        for m in robot.motors:
            m.moving_speed = 50
            m.pid = (4, 2, 0)
            m.torque_limit = 70.
            m.led = 'off'
