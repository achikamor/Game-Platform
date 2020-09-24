import numpy
import Constants
import students_files.first_player as player_1
import students_files.second_player as player_2
import logging
import copy


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
            logging.info("calling function " + str(player_1.play.__name__) + " from module " + str(player_1.__name__))
            board = player_1.play(board,Constants.BOARD_SIZE,Constants.first_player_sign,Constants.second_player_sign)
        else:
            logging.info("calling function " + str(player_2.play.__name__) + " from module " + str(player_2.__name__))
            board = player_2.play(board,Constants.BOARD_SIZE,Constants.second_player_sign,Constants.first_player_sign)
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