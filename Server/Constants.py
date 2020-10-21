from enum import Enum


class MapLevel(Enum):
    One = "1"
    Two = "2"
    Three = "3"
    Four = "4"
    Five = "5"


class ComputerLevel(Enum):
    Easy = "Easy"
    Medium = "Medium"
    Hard = "Hard"


class MapObjectOptions(Enum):
    Empty = "0"
    Obstacle = "1"
    PlayerOne = "2"
    PlayerTwo = "3"
    Door = "4"


class DirectionsVector(Enum):
    UP = (-1, 0)
    DOWN = (1, 0)
    LEFT = (0, -1)
    RIGHT = (0, 1)


class GameOptions(Enum):
    FirstPlayerWin = "first_player"
    SecondPlayerWin = "second_player"
    Draw = "draw"
    Loss = "loss"
    Running = "running"
    FirstPlayerTimeOut = "first_player_time_out"
    SecondPlayerTimeOut = "Second_player_time_out"
    FirstPlayerException = "first_player_exception"
    SecondPlayerException = "second_player_exception"


class TimeoutException(Exception):
    def __init__(self, msg=''):
        self.msg = msg


# Change it on production
BASE_PATH = r"C:\Ben\Nizanim\GamePlatform\Game-Platform\Server"
GAME_PATH = "Games"
MAP_PATH = "Maps"
COMPUTER_PATH = "ComputerCode"
INIT_FILE_NAME = "init.py"
FIRST_PLAYER_MODULE_NAME = "first_player.py"
SECOND_PLAYER_MODULE_NAME = "second_player.py"

BOMBS_STARTING_AMOUNT = 1
BOMBS_TURNS_UNTIL_EXPLODE = 3
HOT_DISTANCE_VALUE = 2
WARM_DISTANCE_VALUE = 4

MAX_TURN_PLAYED = 60
HIT_OBSTACLE_FREEZE_TIME = 5
BOMB_EXPLOSION_FREEZE_TIME = 10
BOMB_EXPLOSION_DISTANCE = 1

STUDENT_FUNCTION_MAX_TIME = 5

MAZE_WALL_BUFFER = 1
