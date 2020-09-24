import numpy
import Constants
import logging
import copy
import importlib.util


def play_game(first_player, second_player):
    board = init_board()
    steps_played = 0
    game_moves = []
    game_over_normally = True
    is_first_player_turn = True
    while not game_over(steps_played):
        steps_played += 1
        logging.info("playing step number :" + str(steps_played))
        logging.info("current board state is " + str(board))
        if is_first_player_turn:
            logging.info("calling function " + str(first_player.play.__name__) + " from module " + str(first_player.__name__))
            board = first_player.play(board,Constants.BOARD_SIZE,Constants.first_player_sign,Constants.second_player_sign)
        else:
            logging.info("calling function " + str(second_player.play.__name__) + " from module " + str(second_player.__name__))
            board = second_player.play(board,Constants.BOARD_SIZE,Constants.second_player_sign,Constants.first_player_sign)
        game_moves.append(create_turn_snapshot(board))
        is_first_player_turn = not is_first_player_turn

    return game_moves


def init_board():
    logging.info("init current game board")
    return numpy.full([Constants.BOARD_SIZE, Constants.BOARD_SIZE],Constants.empty_sign)


def game_over(steps_played):
    return steps_played == 9


def create_turn_snapshot(board):
    return copy.deepcopy(board)


def import_student_files(module_name):
    spec = importlib.util.spec_from_file_location(module_name, str(Constants.BASE_PATH + r"\\" + module_name))
    foo = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(foo)

    return foo
