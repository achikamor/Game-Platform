from player_in_game import PlayerInGame
from game_map import GameMap
import shutil
import os
from typing import Tuple
import uuid
import random
from werkzeug.utils import secure_filename
import Constants
import importlib.util
import numpy


def import_student_code(module_name: str, file_path: str) -> PlayerInGame:
    spec = importlib.util.spec_from_file_location(module_name, file_path)
    foo = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(foo)
    return PlayerInGame(foo.play)


def create_game_directory(base_path: str) -> str:
    directory_name = str(uuid.uuid4())
    full_directory_name = os.path.join(base_path, directory_name)
    os.mkdir(full_directory_name)
    # copy maze_game interface for student
    shutil.copy(os.path.join(Constants.BASE_PATH,Constants.STUDENT_INTERFACE_FILE),
                os.path.join(full_directory_name, Constants.STUDENT_INTERFACE_FILE))
    filename = os.path.join(full_directory_name, Constants.INIT_FILE_NAME)
    open(filename, "a").close()
    return full_directory_name


def save_student_code(directory_path: str, file_name: str, player_file) -> None:
    file_name = secure_filename(file_name)
    player_file.save(os.path.join(directory_path, file_name))


def init_game(map_file_path: str,
              first_player_file_path: str,
              second_player_file_path: str) -> Tuple[GameMap, PlayerInGame, PlayerInGame]:
    # init map with padding of 1 outline of obstacles
    first_player = import_student_code(Constants.FIRST_PLAYER_MODULE_NAME, first_player_file_path)
    second_player = import_student_code(Constants.SECOND_PLAYER_MODULE_NAME, second_player_file_path)

    with open(map_file_path, "r") as file:
        lines = file.read().splitlines()
        map_obstacles = numpy.full((len(lines) + Constants.MAZE_WALL_BUFFER * 2,
                                   len(lines) + Constants.MAZE_WALL_BUFFER * 2),
                                   fill_value=True)
        map_obstacles[Constants.MAZE_WALL_BUFFER:len(lines) + Constants.MAZE_WALL_BUFFER,
        Constants.MAZE_WALL_BUFFER:len(lines) + Constants.MAZE_WALL_BUFFER] = \
            numpy.full((len(lines), len(lines)), fill_value=False)
        curr_row = Constants.MAZE_WALL_BUFFER
        door_options = []
        player_one_options = []
        player_two_options = []
        for curr_line in lines:
            values = curr_line.split(" ")
            curr_column = Constants.MAZE_WALL_BUFFER
            for curr_value in range(len(values)):
                if values[curr_value] == Constants.MapObjectOptions.Obstacle.value:
                    map_obstacles[curr_row][curr_column] = True
                elif values[curr_value] == Constants.MapObjectOptions.PlayerOne.value:
                    player_one_options.append((curr_row, curr_column))
                elif values[curr_value] == Constants.MapObjectOptions.PlayerTwo.value:
                    player_two_options.append((curr_row, curr_column))
                elif values[curr_value] == Constants.MapObjectOptions.Door.value:
                    door_options.append((curr_row, curr_column))

                curr_column += 1
            curr_row += 1

    player_one_location = random.choice(player_one_options)
    player_two_location = random.choice(player_two_options)
    door_location = random.choice(door_options)

    first_player.set_location(player_one_location)
    second_player.set_location(player_two_location)
    maze = GameMap(map_obstacles, door_location)
    first_player.init_visited_cells_matrix(len(map_obstacles))
    second_player.init_visited_cells_matrix(len(map_obstacles))

    return maze, first_player, second_player


def randomize_map(directory_path: str) -> str:
    return os.path.join(directory_path, random.choice(os.listdir(directory_path)))


def copy_computer_code_to_game(game_file_path: str, computer_code_path: str) -> None:
    shutil.copy(computer_code_path, game_file_path)


def delete_game(directory_path: str) -> None:
    try:
        shutil.rmtree(directory_path)
    except Exception as e:
        print("Deletion of the directory %s failed" % directory_path)
        print(str(e))
    else:
        print("Successfully deleted the directory %s" % directory_path)
