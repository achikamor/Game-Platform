from typing import List


class GameMap:
    def __init__(self, game_map: List[bool][bool], door_location : (int, int)):
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

    def is_free_to_move(self, location : (int , int)) -> bool:
        return self._map_obstacles[location[0]][location[1]]