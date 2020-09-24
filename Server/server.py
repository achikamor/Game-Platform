from flask import Flask, Response,jsonify
import logging
import GameManager
import Constants
app = Flask(__name__)
logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)


@app.route('/')
def hello_world():
    first_player = GameManager.import_student_files(Constants.FIRST_PLAYER_MODULE_NAME)
    second_player = GameManager.import_student_files(Constants.SECOND_PLAYER_MODULE_NAME)
    result = GameManager.play_game(first_player,second_player)
    logging.info("finish to run the game")
    return str(result)


if __name__ == '__main__':
    logger.info("welcome to my flask server")
    app.run(debug=True)