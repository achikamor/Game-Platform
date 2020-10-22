from flask import Flask, jsonify, request
import logging
import game_engine
import Constants, game_initializer
import os

app = Flask(__name__)
logger = logging.getLogger(__name__)
logging.basicConfig(format='%(asctime)s :: %(levelname)s :: %(funcName)s :: %(lineno)d :: %(message)s',level=logging.INFO, filename="log.txt")


@app.route('/game')
def run_maze():
    logging.info("got a call to route : run maze")
    logging.info("got request from client")
    logging.info("request data is " + str(request.data))
    #if request.method == "POST":
    # files = request.files['file']
    # directory_name = game_initializer.create_game_directory(os.path.join(Constants.BASE_PATH, Constants.GAME_PATH))
    # game_initializer.save_student_code(directory_name, Constants.FIRST_PLAYER_MODULE_NAME, files[0])
    # if len(files) == 1:
    #     computer_level = Constants.ComputerLevel.Easy.value
    #     game_initializer.copy_computer_code_to_game(os.path.join(Constants.BASE_PATH,
    #                                                              Constants.ComputerCode,
    #                                                              str(computer_level),
    #                                                              Constants.SECOND_PLAYER_MODULE_NAME), os.path.join(directory_name,
    #                                                                                                                 Constants.SECOND_PLAYER_MODULE_NAME))
    # else:
    #     game_initializer.save_student_code(directory_name,Constants.SECOND_PLAYER_MODULE_NAME, files[1])
    game_level = Constants.MapLevel.One ###### change to level from request and change enum value
    game_level_map_path = os.path.join(Constants.BASE_PATH, Constants.MAP_PATH, Constants.MapLevel(game_level).value)
    map_path = game_initializer.randomize_map(game_level_map_path)
        #result = game_initializer.init_game(map_path,
                                            #os.path.join(directory_name, Constants.FIRST_PLAYER_MODULE_NAME),
                                            #os.path.join(directory_name, Constants.SECOND_PLAYER_MODULE_NAME))
    result = run_mock(map_path)
    game_maze = result[0]
    first_player = result[1]
    second_player = result[2]
    game_turns = game_engine.play_game(game_maze, first_player, second_player)
        #game_initializer.delete_game(directory_name)

    logging.info("finish to run the game")
    logging.info("turns send to server are " + str(game_turns))
    return jsonify({"game_turns": game_turns})


def run_mock(map_path: str):
    return game_initializer.init_game(map_path,
                                      r"C:\Ben\Nizanim\GamePlatform\Game-Platform\Server\Games\Mock\first_player.py",
                                      r"C:\Ben\Nizanim\GamePlatform\Game-Platform\Server\Games\Mock\second_player.py")


if __name__ == '__main__':
    logger.info("welcome to my flask server")
    app.run(debug=True)