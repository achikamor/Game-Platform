from Server.maze_game import Action, Direction
from Server.Constants import DirectionsVector
from Server import Constants
import logging
import numpy
from Server.maze_game import BaseGamePlayer
from Server import game_engine


class PlayerInGame:
    def __init__(self, player_code: callable()):
        self._play_turn = player_code
        self._bombs_left = Constants.BOMBS_STARTING_AMOUNT
        self._visited_cells = None
        self._stop_turns_left = 0
        self._last_move = None
        self._position = None

    def init_visited_cells_matrix(self, map_size: int) -> None:
        self._visited_cells = numpy.full((map_size, map_size), fill_value=False)

    def set_location(self, player_location: (int, int)) -> None:
        self._position = player_location

    def get_location(self) -> (int, int):
        return self._position

    def move(self, direction: Constants.DirectionsVector) -> None:
        self.set_location((self._position[0] + direction[0], self._position[1] + direction[1]))
        self.set_cell_as_visited(self._position)

    def set_cell_as_visited(self, cell_location: (int, int)) -> None:
        self._visited_cells[cell_location[0]][cell_location[1]] = True

    def can_drop_bomb(self) -> bool:
        return self._bombs_left > 0

    def can_play(self) -> bool:
        return self._stop_turns_left == 0

    def wait_turn(self) -> None:
        if self._stop_turns_left > 0:
            self._stop_turns_left -= 1

    def freeze(self, freeze_turn_num: int) -> None:
        self._stop_turns_left += freeze_turn_num

    def is_visit_cell(self, direction: Direction) -> bool:
        current_direction = game_engine.convert_direction_to_direction_vector(direction)
        return self._visited_cells[self._position[0] + current_direction[0]][self._position[1] + current_direction[1]]

    def get_last_move(self) -> Direction:
        return self._last_move

    def set_last_move(self, direction: Direction) -> None:
        self._last_move = direction

    def play(self, player: BaseGamePlayer) -> Action:
        return self._play_turn(player)
