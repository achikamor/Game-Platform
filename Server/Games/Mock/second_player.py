from Server.Games.Mock.maze_game import Direction, Action, DoorDistanceStatus
from Server.Games.Mock.maze_game import BaseGamePlayer


def play(player: BaseGamePlayer) -> Action:
    if player.check_movement(Direction.UP) and not player.check_old_steps(Direction.UP):
        return Action.MOVE_UP
    elif player.check_movement(Direction.DOWN) and not player.check_old_steps(Direction.DOWN):
        return Action.MOVE_DOWN
    elif player.check_movement(Direction.LEFT) and not player.check_old_steps(Direction.LEFT):
        return Action.MOVE_LEFT
    else:
        return Action.MOVE_RIGHT
