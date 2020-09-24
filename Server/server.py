from flask import Flask, Response,jsonify
import logging
import GameManager

app = Flask(__name__)
logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)


@app.route('/')
def hello_world():
    result = GameManager.play_game(1,2)
    logging.info("finish to run the game")
    return str(result)


if __name__ == '__main__':
    logger.info("welcome to my flask server")
    app.run(debug=True)