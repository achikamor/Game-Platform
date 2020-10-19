from enum import Enum


class ComputerLevels(Enum):
    Easy = 1
    Medium = 2
    Hard = 3


class DirectionsVector(Enum):
    UP = (-1, 0)
    DOWN = (1, 0)
    LEFT = (0, 1)
    RIGHT = (0, -1)


class GameEndOptions(Enum):
    FirstPlayerWin = "player1"
    SecondPlayerWin = "player2"
    Draw = "draw"
    lose = "loss"


# Change it on production
BASE_PATH = r"C:\Ben\Nizanim\GamePlatform\Game-Platform\Server\students_files"

FIRST_PLAYER_MODULE_NAME = "first_player.py"
SECOND_PLAYER_MODULE_NAME = "second_player.py"
BOMBS_STARTING_AMOUNT = 1
BOMBS_TURNS_UNTIL_EXPLODE = 3
HOT_DISTANCE_VALUE = 2
WARM_DISTANCE_VALUE = 4

MAX_TURN_PLAYED = 60
HIT_OBSTACLE_FREEZE_TIME = 5

