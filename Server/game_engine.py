import numpy
import logging
import copy
import Server.Constants as Constants
from Server.game_map import GameMap
from Server.player_in_game import PlayerInGame
from Server.student_game_player import StudentGamePlayer
from Server.maze_game import Action, Direction
from Server.Constants import DirectionsVector, TimeoutException
from contextlib import contextmanager
import threading
import _thread


def play_game(maze: GameMap, first_player: PlayerInGame, second_player: PlayerInGame):
    current_turn_number = 0
    game_turns = []
    first_bomb_turns_to_explode = None
    second_bomb_turn_to_explode = None
    game_status = Constants.GameOptions.Running
    if first_player is None:
        game_status = Constants.GameOptions.FirstPlayerException
        # if first player code doesnt imported successfully, there is no game
        game_turns.append([None,False,False,game_status])
    elif second_player is None:
        game_status = Constants.GameOptions.SecondPlayerException
        # if secomd player code doesnt imported successfully, there is no game
        game_turns.append([None, False, False, game_status])

    is_game_interrupted = False
    while game_status == Constants.GameOptions.Running:
        logging.info("trying to play turn number : " + str(current_turn_number))
        logging.info("first player location is :" + str(first_player.get_location()))
        logging.info("second player location is :" + str(second_player.get_location()))

        if first_player.can_play():
            try:
                with time_limit(Constants.STUDENT_FUNCTION_MAX_TIME, "first_player play turn"):
                    turn_player = StudentGamePlayer(create_turn_snapshot(maze), first_player)
                    wanted_action = first_player.play(turn_player)
                    if wanted_action.value != Action.DROP_BOMB.value:
                        logging.info("player one trying to move "+ str(wanted_action.value))
                        direction_to_move = convert_action_to_direction_vector(wanted_action)
                        if turn_player.check_movement_with_direction_vector(direction_to_move):
                            logging.info("player one moved " + str(wanted_action.value) + " successfully")
                            first_player.move(direction_to_move)
                        else:
                            logging.info("first player freeze")
                            first_player.freeze(Constants.HIT_OBSTACLE_FREEZE_TIME)
                    else:
                        logging.info("first player try to drop a bomb at location " + str(first_player.get_location()))
                        if first_player.can_drop_bomb():
                            maze.set_first_player_bomb(first_player.get_location())
                            first_player.reduce_bomb_count()
                            first_bomb_turns_to_explode = Constants.BOMBS_TURNS_UNTIL_EXPLODE
                            logging.info("first player dropped a bomb successfully")
            # if student code contains exception handling, it will not work
            except TimeoutException as e:
                game_status = Constants.GameOptions.FirstPlayerTimeOut
                is_game_interrupted = True
                pass
            except Exception as e:
                game_status = Constants.GameOptions.FirstPlayerException
                is_game_interrupted = True
                logging.error("first player got exception : " + str(e))
                pass
        else:
            first_player.wait_turn()

        if not is_game_interrupted and second_player.can_play():
            try:
                with time_limit(Constants.STUDENT_FUNCTION_MAX_TIME, "second_player play turn"):
                    turn_player = StudentGamePlayer(create_turn_snapshot(maze), second_player)
                    wanted_action = second_player.play(turn_player)
                    if wanted_action.value != Action.DROP_BOMB.value:
                        logging.info("player two trying to move "+ str(wanted_action.value))
                        direction_to_move = convert_action_to_direction_vector(wanted_action)
                        if turn_player.check_movement_with_direction_vector(direction_to_move):
                            second_player.move(direction_to_move)
                            logging.info("player two moved " + str(wanted_action.value) + " successfully")
                        else:
                            logging.info("second player freeze")
                            second_player.freeze(Constants.HIT_OBSTACLE_FREEZE_TIME)
                    else:
                        logging.info("second player try to drop  a bomb at location " + str(second_player.get_location()))
                        if second_player.can_drop_bomb():
                            maze.set_second_player_bomb(second_player.get_location())
                            second_player.reduce_bomb_count()
                            second_bomb_turn_to_explode = Constants.BOMBS_TURNS_UNTIL_EXPLODE
                            logging.info("second player dropped a bomb successfully")
            # if student code contains exception handling, it will not work
            except TimeoutException as e:
                game_status = Constants.GameOptions.SecondPlayerTimeOut
                is_game_interrupted = True
                pass
            except Exception as e:
                game_status = Constants.GameOptions.SecondPlayerException
                is_game_interrupted = True
                logging.error("second player got exception : " + str(e))
                pass
        else:
            second_player.wait_turn()

        if first_bomb_turns_to_explode is not None:
            if first_bomb_turns_to_explode == 0:
                bomb(maze, first_player, second_player, maze.get_first_player_bomb())
                first_bomb_turns_to_explode = None
                maze.set_first_player_bomb(None)
            else:
                first_bomb_turns_to_explode -= 1

        if second_bomb_turn_to_explode is not None:
            if second_bomb_turn_to_explode == 0:
                bomb(maze, first_player, second_player, maze.get_second_player_bomb())
                second_bomb_turn_to_explode = None
                maze.set_second_player_bomb(None)
            else:
                second_bomb_turn_to_explode -= 1

        maze_for_ui = convert_map_status_to_numbers_for_ui(maze, first_player, second_player)

        logging.info("finish to play turn number : " + str(current_turn_number))
        logging.info("first player location is :" + str(first_player.get_location()))
        logging.info("second player location is :" + str(second_player.get_location()))
        logging.info("door location is " + str(maze.get_door_location()))
        logging.info("map  is " + str(maze_for_ui))
        current_turn_number += 1
        if not is_game_interrupted:
            game_status = get_game_status(maze, first_player, second_player, current_turn_number)
        current_turn = [maze_for_ui, not first_player.can_play(), not second_player.can_play(), game_status.value]
        game_turns.append(current_turn)

    return game_turns


def get_game_status(maze: GameMap,
                    first_player: PlayerInGame,
                    second_player: PlayerInGame, turn_number: int) -> Constants.GameOptions:

    game_status = Constants.GameOptions.Running
    if turn_number > Constants.MAX_TURN_PLAYED:
        game_status = Constants.GameOptions.Loss
    elif first_player.get_location() == maze.get_door_location():
        if second_player.get_location() == maze.get_door_location():
            game_status = Constants.GameOptions.Draw
        else:
            game_status = Constants.GameOptions.FirstPlayerWin
    elif second_player.get_location() == maze.get_door_location():
        game_status = Constants.GameOptions.SecondPlayerWin

    return game_status


def bomb(maze: GameMap, first_player: PlayerInGame, second_player: PlayerInGame, bomb_location: (int, int)) -> None:
    logging.info("trying to explode bomb at location " + str(bomb_location))
    # checks if first player is within bomb explosion area
    if abs(bomb_location[0] - first_player.get_location()[0]) <= 1 and \
       abs(bomb_location[1] - first_player.get_location()[1]) <= 1:
        first_player.freeze(Constants.BOMB_EXPLOSION_FREEZE_TIME)

    if abs(bomb_location[0] - second_player.get_location()[0]) <= 1 and \
       abs(bomb_location[1] - second_player.get_location()[1]) <= 1:
        second_player.freeze(Constants.BOMB_EXPLOSION_FREEZE_TIME)

    maze.remove_obstacles_area(Constants.BOMB_EXPLOSION_DISTANCE, bomb_location)


def create_turn_snapshot(board: GameMap) -> GameMap:
    return copy.deepcopy(board)


def convert_direction_to_direction_vector(direction: Direction) -> DirectionsVector:
    if direction.value == Direction.UP.value:
        return DirectionsVector.UP.value
    elif direction.value == Direction.DOWN.value:
        return DirectionsVector.DOWN.value
    elif direction.value == Direction.LEFT.value:
        return DirectionsVector.LEFT.value
    elif direction.value == Direction.RIGHT.value:
        return DirectionsVector.RIGHT.value
    else:
        logging.error("error while converting direction to direction vector. got unexpected direction")
        logging.error(str(direction))


def convert_direction_vector_to_direction(direction: DirectionsVector) -> Direction:
    if direction == DirectionsVector.UP.value:
        return Direction.UP
    elif direction == DirectionsVector.DOWN.value:
        return Direction.DOWN
    elif direction == DirectionsVector.LEFT.value:
        return Direction.LEFT
    elif direction == DirectionsVector.RIGHT.value:
        return Direction.RIGHT
    else:
        logging.error("error while converting direction vector to direction. got unexpected direction")


def convert_action_to_direction_vector(wanted_action: Action) -> DirectionsVector:
    if wanted_action.value == Action.MOVE_UP.value:
        return DirectionsVector.UP.value
    elif wanted_action.value == Action.MOVE_DOWN.value:
        return DirectionsVector.DOWN.value
    elif wanted_action.value == Action.MOVE_LEFT.value:
        return DirectionsVector.LEFT.value
    elif wanted_action.value == Action.MOVE_RIGHT.value:
        return DirectionsVector.RIGHT.value
    else:
        logging.error(
            "error while converting action to direction vector. got unexpected action : " + str(wanted_action))


def convert_map_status_to_numbers_for_ui(maze: GameMap,
                                         first_player: PlayerInGame,
                                         second_player: PlayerInGame):

    logging.info("trying to convert current map for ui")
    map_for_ui = numpy.full((len(maze.get_map()) - Constants.MAZE_WALL_BUFFER * 2,
                             len(maze.get_map()) - Constants.MAZE_WALL_BUFFER * 2),
                            fill_value=0,
                            dtype=int)
    first_bomb_location = maze.get_first_player_bomb()
    second_bomb_location = maze.get_second_player_bomb()
    door_location = maze.get_door_location()

    for row in range(Constants.MAZE_WALL_BUFFER, len(map_for_ui) + Constants.MAZE_WALL_BUFFER):
        for column in range(Constants.MAZE_WALL_BUFFER, len(map_for_ui) + Constants.MAZE_WALL_BUFFER):
            current_position = (row, column)
            cell_value = ""

            cell_value += "1" if maze.get_map()[row][column] else "0"

            cell_value += "1" if first_player.get_location() == current_position else "0"

            cell_value += "1" if second_player.get_location() == current_position else "0"

            cell_value += "1" if first_bomb_location == current_position else "0"

            cell_value += "1" if second_bomb_location == current_position else "0"

            cell_value += "1" if door_location == current_position else "0"

            # convert from binary to int
            map_for_ui[row - Constants.MAZE_WALL_BUFFER][column - Constants.MAZE_WALL_BUFFER] = int(cell_value, 2)

    return map_for_ui.tolist()


@contextmanager
def time_limit(seconds, msg=''):
    timer = threading.Timer(seconds, lambda: _thread.interrupt_main())
    timer.start()
    try:
        yield
    except KeyboardInterrupt:
        raise TimeoutException("Timed out for {}".format(msg))
    finally:
        # if the action ends in specified time, timer is canceled
        timer.cancel()
