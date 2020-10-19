from abc import ABC, abstractmethod
from enum import Enum


class Direction(Enum):
    UP = "up"
    DOWN = "down"
    LEFT = "left"
    RIGHT = "right"


class Action(Enum):
    MOVE_UP = "up"
    MOVE_DOWN = "down"
    MOVE_LEFT = "left"
    MOVE_RIGHT = "right"
    DROP_BOMB = "bomb"


class DoorDistanceStatus(Enum):
    HOT = "hot"
    WARM = "warm"
    COLD = "cold"


class BaseGamePlayer(ABC):
    @abstractmethod
    def check_movement(self, direction : Direction) -> bool:
        pass

    @abstractmethod
    def flash_light(self) -> Direction:
        pass

    @abstractmethod
    def check_old_steps(self, direction : Direction) -> bool:
        pass

    @abstractmethod
    def doors_direction(self, direction : Direction) -> bool:
        pass

    @abstractmethod
    def distance_from_door(self) -> DoorDistanceStatus:
        pass

    @abstractmethod
    def distance_from_bomb(self) -> int:
        pass

    @abstractmethod
    def bombs_direction(self, direction : Direction) -> bool:
        pass
