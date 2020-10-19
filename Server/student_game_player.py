from Server.maze_game import Direction, BaseGamePlayer, DoorDistanceStatus
from Server.player_in_game import PlayerInGame
from Server.game_map import GameMap
from Server import Constants, game_engine
import logging
import math
from Server.Constants import DirectionsVector


class StudentGamePlayer(BaseGamePlayer):
    def __init__(self, game_map: GameMap, current_player: PlayerInGame):
        self.map = game_map
        self.player = current_player

    def flash_light(self) -> Direction:
        return self.player.get_last_move().value

    def check_old_steps(self, direction: Direction) -> bool:
        return self.player.is_visit_cell(direction)

    def doors_direction(self, direction: Direction) -> bool:
        logging.info("got doors direction checks. player position : " + str(self.player.get_location()) +
                     " and direction is + :" + str(direction.value))
        door_location = self.map.get_door_location()
        if direction == Direction.UP:
            return door_location[0] < self.player.get_location()[0]
        elif direction == Direction.DOWN:
            return door_location[0] > self.player.get_location()[0]
        elif direction == Direction.LEFT:
            return door_location[1] < self.player.get_location()[1]
        elif direction == Direction.RIGHT:
            return door_location[1] > self.player.get_location()[1]
        else:
            logging.error("unexpected direction : " + str(direction.value))

    def distance_from_door(self) -> DoorDistanceStatus:
        door_location = self.map.get_door_location()
        distance = math.sqrt((math.pow(door_location[0] - self.player.get_location()[0], 2))
                             + math.pow(door_location[1] - self.player.get_location()[1], 2))

        if distance <= Constants.HOT_DISTANCE_VALUE:
            return DoorDistanceStatus.HOT.value
        elif distance <= Constants.WARM_DISTANCE_VALUE:
            return DoorDistanceStatus.WARM.value
        else:
            return DoorDistanceStatus.COLD.value

    def distance_from_bomb(self) -> int:
        first_bomb_location = self.map.get_first_player_bomb()
        second_bomb_location = self.map.get_second_player_bomb()

        if self.player.get_location() == first_bomb_location or \
                self.player.get_location() == second_bomb_location:
            return 0
        elif abs(self.player.get_location()[0] - first_bomb_location[0]) <= 1 and \
                abs(self.player.get_location()[1] - first_bomb_location[1]) <= 1:
            return 1
        elif abs(self.player.get_location()[0] - second_bomb_location[0]) <= 1 and \
                abs(self.player.get_location()[1] - second_bomb_location[1]) <= 1:
            return 1
        else:
            return 2

    def bombs_direction(self, direction: Direction) -> bool:
        first_bomb_location = self.map.get_first_player_bomb()
        second_bomb_location = self.map.get_second_player_bomb()

        if direction == Direction.UP:
            return first_bomb_location[0] < self.player.get_location()[0] or \
                   second_bomb_location[0] < self.player.get_location()[0]
        elif direction == Direction.DOWN:
            return first_bomb_location[0] > self.player.get_location()[0] or \
                   second_bomb_location[0] > self.player.get_location()[0]
        elif direction == Direction.LEFT:
            return first_bomb_location[1] < self.player.get_location()[1] or \
                   second_bomb_location[1] < self.player.get_location()[1]
        elif direction == Direction.RIGHT:
            return first_bomb_location[1] > self.player.get_location()[1] or \
                   second_bomb_location[1] > self.player.get_location()[1]

    def check_movement(self, direction: Direction) -> bool:
        new_direction = game_engine.convert_direction_to_direction_vector(direction)
        return self.check_movement_with_direction_vector(new_direction)

    def check_movement_with_direction_vector(self, direction: DirectionsVector) -> bool:
        new_cell_value = (self.player.get_location()[0] + direction[0], self.player.get_location()[1] + direction[1])
        return self.map.get_map()[new_cell_value[0]][new_cell_value[1]].is_free_to_move()
