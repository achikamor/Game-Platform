import random
import logging


def play(board, board_size, player_sign, opponent_player_sign):
    found = False
    while not found:
        number = random.randint(0, 8)
        logging.info("in module first player trying to random number " + str(number) + " and board is " + str(board))
        if board[number // board_size][number % board_size] == 0:
            board[number // board_size][number % board_size] = player_sign
            found = True

    return board