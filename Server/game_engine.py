import numpy
from Server import Constants
import logging
import copy
from Server.game_map import GameMap
from Server.player_in_game import PlayerInGame
from typing import List
from Server.student_game_player import StudentGamePlayer
from Server.maze_game import Action, Direction
from Server.Constants import DirectionsVector, CellValueForUi


def play_game(maze: GameMap, first_player: PlayerInGame, second_player: PlayerInGame) -> List[int][int]:
    current_turn_number = 0
    game_turns = []
    first_bomb_turns_to_explode = None
    second_bomb_turn_to_explode = None

    while not is_game_over(maze, first_player, second_player, current_turn_number):
        if first_player.can_play():
            turn_player = StudentGamePlayer(create_turn_snapshot(maze), first_player)
            wanted_action = first_player.play(turn_player)
            if wanted_action != Action.DROP_BOMB:
                direction_to_move = convert_action_to_direction_vector(wanted_action)
                if turn_player.check_movement_with_direction_vector(direction_to_move):
                    first_player.move(direction_to_move)
                else:
                    first_player.freeze(Constants.HIT_OBSTACLE_FREEZE_TIME)
            else:
                if first_player.can_drop_bomb():
                    maze.set_first_player_bomb(first_player.get_location())
                    first_bomb_turns_to_explode = Constants.BOMBS_TURNS_UNTIL_EXPLODE
        else:
            first_player.wait_turn()

        if first_bomb_turns_to_explode is not None:
            if first_bomb_turns_to_explode == 0:
                bomb(maze, first_player, second_player, maze.get_first_player_bomb())
                first_bomb_turns_to_explode = None
                maze.set_first_player_bomb(None)
            else:
                first_bomb_turns_to_explode -= 1

        if second_bomb_turn_to_explode is not None and second_bomb_turn_to_explode == 0:
            bomb(maze, first_player, second_player, maze.get_second_player_bomb())


def is_game_over(maze: GameMap, first_player: PlayerInGame, second_player: PlayerInGame, turn_number: int) -> bool:
    door_location = maze.get_door_location()
    return first_player.position == door_location or \
           second_player.position == door_location or \
           turn_number == Constants.MAX_TURN_PLAYED


def bomb(maze: GameMap, first_player: PlayerInGame, second_player: PlayerInGame, bomb_location: (int, int)) -> None:
    pass


def create_turn_snapshot(board: GameMap) -> GameMap:
    return copy.deepcopy(GameMap)


def delete_game(directory_path: str) -> None:
    pass


def convert_direction_to_direction_vector(direction: Direction) -> DirectionsVector:
    if direction == Direction.UP:
        return DirectionsVector.UP.value
    elif direction == Direction.DOWN:
        return DirectionsVector.DOWN.value
    elif direction == Direction.LEFT:
        return DirectionsVector.LEFT.value
    elif direction == Direction.RIGHT:
        return DirectionsVector.RIGHT.value
    else:
        logging.error("error while converting direction to direction vector. got unexpected direction")


def convert_action_to_direction_vector(wanted_action: Action) -> DirectionsVector:
    if wanted_action == Action.MOVE_UP:
        return DirectionsVector.UP.value
    elif wanted_action == Action.MOVE_DOWN:
        return DirectionsVector.DOWN.value
    elif wanted_action == Action.MOVE_LEFT:
        return DirectionsVector.LEFT.value
    elif wanted_action == Action.MOVE_RIGHT:
        return DirectionsVector.RIGHT.value
    else:
        logging.error(
            "error while converting action to direction vector. got unexpected action : " + str(wanted_action))


def convert_map_status_to_numbers_for_ui(maze: GameMap,
                                         first_player: PlayerInGame,
                                         second_player: PlayerInGame) -> List[int][int]:
    map_for_ui = numpy.full((len(maze), len(maze[0])), fill_value=0, dtype=int)
    first_bomb_location = maze.get_first_player_bomb()
    second_bomb_location = maze.get_second_player_bomb()
    door_location = maze.get_door_location()

    for row in range(len(maze)):
        for column in range(len(maze[0])):
            current_position = (row, column)
            cell_value = ""

            cell_value += "1" if maze[row][column] else "0"

            cell_value += "1" if first_player.get_location() == current_position else "0"

            cell_value += "1" if second_player.get_location() == current_position else "0"

            cell_value += "1" if first_bomb_location == current_position else "0"

            cell_value += "1" if second_bomb_location == current_position else "0"

            cell_value += "1" if door_location == current_position else "0"

            # convert from binary to int
            map_for_ui[row][column] = int(cell_value, 2)
