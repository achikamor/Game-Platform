from maze_game import Direction, Action, DoorDistanceStatus
from maze_game import BaseGamePlayer


def play(player: BaseGamePlayer) -> Action:
    if player.check_movement(Direction.UP) and not player.check_old_steps(Direction.UP) and \
            player.flash_light() != Direction.DOWN.value and player.doors_direction(Direction.UP):
        return Action.MOVE_UP
    elif player.check_movement(Direction.DOWN) and not player.check_old_steps(Direction.DOWN) and \
            player.flash_light() != Direction.UP.value and player.doors_direction(Direction.DOWN):
        return Action.MOVE_DOWN
    elif player.check_movement(Direction.LEFT) and not player.check_old_steps(Direction.LEFT) and \
            player.flash_light() != Direction.RIGHT.value and player.doors_direction(Direction.LEFT):
        return Action.MOVE_LEFT
    else:
        return Action.MOVE_RIGHT
