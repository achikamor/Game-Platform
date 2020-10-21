from typing import List
import numpy
import logging

class GameMap:
    def __init__(self, game_map: numpy.ndarray, door_location: (int, int)):
        self._map_obstacles = game_map
        self._first_player_bomb_location = None
        self._second_player_bomb_location = None
        self._door = door_location

    def get_door_location(self) -> (int, int):
        return self._door

    def get_first_player_bomb(self) -> (int, int):
        return self._first_player_bomb_location

    def get_second_player_bomb(self) -> (int, int):
        return self._second_player_bomb_location

    def set_first_player_bomb(self, bomb_location: (int, int)) -> None:
        self._first_player_bomb_location = bomb_location

    def set_second_player_bomb(self, bomb_location: (int, int)) -> None:
        self._second_player_bomb_location = bomb_location

    def is_free_to_move(self, location: (int, int)) -> bool:
        return not self._map_obstacles[location[0]][location[1]]

    def get_map(self):
        return self._map_obstacles

    def remove_obstacles_area(self, explosion_distance: int, bomb_location: (int, int)) -> None:
        for row in range(bomb_location[0] - explosion_distance, bomb_location[0] + explosion_distance + 1):
            for column in range(bomb_location[1] - explosion_distance, bomb_location[1] + explosion_distance +1):
                if row == bomb_location[0] and column == bomb_location[1]:
                    pass
                elif self._map_obstacles[row][column] and not self.is_in_outline((row, column)):
                    self._map_obstacles[row][column] = False

    def is_in_outline(self, location: (int, int)) -> bool:
        return location[0] <= 0 or location[0] >= len(self._map_obstacles) or \
            location[1] <= 0 or location[1] >= len(self._map_obstacles[0])