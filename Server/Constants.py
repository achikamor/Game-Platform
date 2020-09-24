from enum import Enum


class ComputerLevels(Enum):
    Easy = 1
    Medium = 2
    Hard = 3


# Change if it is on linux
BASE_PATH = r"C:\Ben\Nizanim\GamePlatform\Game-Platform\Server\students_files"
BOARD_SIZE = 3

first_player_sign = 1
second_player_sign = 2
empty_sign = 0

FIRST_PLAYER_MODULE_NAME = "first_player.py"
SECOND_PLAYER_MODULE_NAME = "second_player.py"
