from flask import Flask, Response,jsonify
import logging
from Server import game_engine, Constants

app = Flask(__name__)
logger = logging.getLogger(__name__)
logging.basicConfig(format='%(asctime)s :: %(levelname)s :: %(funcName)s :: %(lineno)d :: %(message)s',level=logging.INFO, filename="log.txt")


@app.route('/')
def hello_world():
    logging.info("got a call to route : hello world ")
    first_player = game_engine.import_student_files(Constants.FIRST_PLAYER_MODULE_NAME)
    second_player = game_engine.import_student_files(Constants.SECOND_PLAYER_MODULE_NAME)
    result = game_engine.play_game(first_player, second_player)
    logging.info("finish to run the game")
    return str(result)


if __name__ == '__main__':
    logger.info("welcome to my flask server")
    app.run(debug=True)