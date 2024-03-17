from enum import Enum
import random


class Position(Enum):
    INTERN = 0
    JUNIOR_DEVELOPER = 10000
    MIDDLE_DEVELOPER = 15000
    SENIOR_DEVELOPER = 20000
    TECHNICAL_DEVELOPER = 30000

    @classmethod
    def to_position(cls, name):
        if name == 'INTERN':
            return Position.INTERN
        elif name == 'JUNIOR_DEVELOPER':
            return Position.JUNIOR_DEVELOPER
        elif name == 'MIDDLE_DEVELOPER':
            return Position.MIDDLE_DEVELOPER
        elif name == 'SENIOR_DEVELOPER':
            return Position.SENIOR_DEVELOPER
        elif name == 'TECHNIC_DEVELOPER':
            return Position.TECHNICAL_DEVELOPER

    @classmethod
    def get_random_position(cls):
        return random.choice(list(Position))
