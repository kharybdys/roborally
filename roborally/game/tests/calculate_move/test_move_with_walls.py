import pytest

from roborally.game.board.board import Board
from roborally.game.board.calculate_move import calculate_move
from roborally.game.board.coord import Coord
from roborally.game.commands.movement import BotHitsWall, BotArrivesAt
from roborally.game.direction import Direction


@pytest.mark.parametrize(
    ("start", "movement_direction", "steps", "wall_at", "arrived_at"),
    [
        (Coord(x=1, y=3), Direction.NORTH, 3, Coord(x=1, y=1), Coord(x=1, y=1)),
        (Coord(x=2, y=2), Direction.NORTH, 2, Coord(x=2, y=1), Coord(x=2, y=1)),
        (Coord(x=3, y=1), Direction.NORTH, 1, Coord(x=3, y=1), Coord(x=3, y=1)),
        (Coord(x=2, y=2), Direction.EAST, 3, Coord(x=4, y=2), Coord(x=4, y=2)),
        (Coord(x=3, y=3), Direction.EAST, 2, Coord(x=4, y=3), Coord(x=4, y=3)),
        (Coord(x=4, y=4), Direction.EAST, 1, Coord(x=4, y=4), Coord(x=4, y=4)),
        (Coord(x=2, y=2), Direction.SOUTH, 3, Coord(x=2, y=4), Coord(x=2, y=4)),
        (Coord(x=3, y=3), Direction.SOUTH, 2, Coord(x=3, y=4), Coord(x=3, y=4)),
        (Coord(x=4, y=4), Direction.SOUTH, 1, Coord(x=4, y=4), Coord(x=4, y=4)),
        (Coord(x=3, y=1), Direction.WEST, 3, Coord(x=1, y=1), Coord(x=1, y=1)),
        (Coord(x=2, y=2), Direction.WEST, 2, Coord(x=1, y=2), Coord(x=1, y=2)),
        (Coord(x=1, y=3), Direction.WEST, 1, Coord(x=1, y=3), Coord(x=1, y=3)),
    ],
)
@pytest.mark.parametrize("board_name", ["six_by_six_with_walls_board"])
def test_bump_into_wall(
    board: Board,
    start: Coord,
    movement_direction: Direction,
    steps: int,
    wall_at: Coord,
    arrived_at: Coord,
):
    commands = calculate_move(
        board=board,
        start=start,
        movement_direction=movement_direction,
        steps=steps,
    )
    assert len(commands) == 2

    bot_hit_wall_command: BotHitsWall | None = None
    bot_arrives_at_command: BotArrivesAt | None = None
    for command in commands:
        if isinstance(command, BotHitsWall):
            bot_hit_wall_command = command
        if isinstance(command, BotArrivesAt):
            bot_arrives_at_command = command

    assert bot_hit_wall_command is not None, "bot hit wall"
    assert bot_hit_wall_command.wall_at == wall_at

    assert bot_arrives_at_command is not None, "bot arrives"
    assert bot_arrives_at_command.arrived_at == arrived_at


@pytest.mark.parametrize(
    ("start", "movement_direction", "steps", "arrived_at"),
    [
        (Coord(x=1, y=4), Direction.NORTH, 3, Coord(x=1, y=1)),
        (Coord(x=2, y=3), Direction.NORTH, 2, Coord(x=2, y=1)),
        (Coord(x=3, y=2), Direction.NORTH, 1, Coord(x=3, y=1)),
        (Coord(x=1, y=2), Direction.EAST, 3, Coord(x=4, y=2)),
        (Coord(x=2, y=3), Direction.EAST, 2, Coord(x=4, y=3)),
        (Coord(x=3, y=4), Direction.EAST, 1, Coord(x=4, y=4)),
        (Coord(x=2, y=1), Direction.SOUTH, 3, Coord(x=2, y=4)),
        (Coord(x=3, y=2), Direction.SOUTH, 2, Coord(x=3, y=4)),
        (Coord(x=4, y=3), Direction.SOUTH, 1, Coord(x=4, y=4)),
        (Coord(x=4, y=1), Direction.WEST, 3, Coord(x=1, y=1)),
        (Coord(x=3, y=2), Direction.WEST, 2, Coord(x=1, y=2)),
        (Coord(x=2, y=3), Direction.WEST, 1, Coord(x=1, y=3)),
    ],
)
@pytest.mark.parametrize("board_name", ["six_by_six_with_walls_board"])
def test_no_hit_wall(
    board: Board,
    start: Coord,
    movement_direction: Direction,
    steps: int,
    arrived_at: Coord,
):
    commands = calculate_move(
        board=board,
        start=start,
        movement_direction=movement_direction,
        steps=steps,
    )
    assert len(commands) == 1

    command = commands[0]
    assert isinstance(command, BotArrivesAt), "bot arrives"
    assert command.arrived_at == arrived_at
