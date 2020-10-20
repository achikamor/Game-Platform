from flask import Flask, Response,jsonify, request
import logging
from Server import game_engine, Constants, game_initializer
import os


app = Flask(__name__)
logger = logging.getLogger(__name__)
logging.basicConfig(format='%(asctime)s :: %(levelname)s :: %(funcName)s :: %(lineno)d :: %(message)s',level=logging.INFO, filename="log.txt")


@app.route('/')
def run_maze():
    logging.info("got a call to route : run maze")
    if request.method == "POST":
        files = request.files['file']
        directory_name = game_initializer.create_game_directory(os.path.join(Constants.BASE_PATH, Constants.GAME_PATH))
        game_initializer.save_student_code(directory_name, Constants.FIRST_PLAYER_MODULE_NAME, files[0])
        game_initializer.save_student_code(directory_name,Constants.SECOND_PLAYER_MODULE_NAME, files[1])
        game_level = Constants.MapLevel.Easy ###### change to level from request and change enum value
        game_level_map_path = os.path.join(Constants.BASE_PATH, Constants.MAP_PATH, Constants.MapLevel(game_level).name)
        map_path = game_initializer.randomize_map(game_level_map_path)
        result = game_initializer.init_game(map_path,
                                            os.path.join(directory_name, Constants.FIRST_PLAYER_MODULE_NAME),
                                            os.path.join(directory_name, Constants.SECOND_PLAYER_MODULE_NAME))
        game_maze = result[0]
        first_player = result[1]
        second_player = result[2]
        game_turns = game_engine.play_game(game_maze, first_player, second_player)
        game_initializer.delete_game(directory_name)



        ######### if computer plays
        os.path.join(Constants.BASE_PATH, Constants.COMPUTER_PATH, Constants.ComputerLevel.Easy.value)
        logging.info("finish to run the game")
        return jsonify(game_turns)


if __name__ == '__main__':
    logger.info("welcome to my flask server")
    app.run(debug=True)