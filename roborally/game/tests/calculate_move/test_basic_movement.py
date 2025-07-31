import pytest

from roborally.game.board.board import Board
from roborally.game.board.calculate_move import calculate_move
from roborally.game.board.coord import Coord
from roborally.game.commands.movement import BotArrivesAt
from roborally.game.direction import Direction


@pytest.mark.parametrize(
    ("start", "movement_direction", "steps", "ends_at"),
    [
        (Coord(x=1, y=2), Direction.NORTH, 2, Coord(x=1, y=0)),
        (Coord(x=2, y=1), Direction.NORTH, 1, Coord(x=2, y=0)),
        (Coord(x=0, y=1), Direction.EAST, 2, Coord(x=2, y=1)),
        (Coord(x=1, y=2), Direction.EAST, 1, Coord(x=2, y=2)),
        (Coord(x=1, y=0), Direction.SOUTH, 2, Coord(x=1, y=2)),
        (Coord(x=2, y=1), Direction.SOUTH, 1, Coord(x=2, y=2)),
        (Coord(x=2, y=1), Direction.WEST, 2, Coord(x=0, y=1)),
        (Coord(x=1, y=2), Direction.WEST, 1, Coord(x=0, y=2)),
    ],
)
@pytest.mark.parametrize("board_name", ["three_by_three_empty_board"])
def test_basic_movement(
    board: Board,
    start: Coord,
    movement_direction: Direction,
    steps: int,
    ends_at: Coord,
):
    commands = calculate_move(
        board=board,
        start=start,
        movement_direction=movement_direction,
        steps=steps,
    )
    assert len(commands) == 1
    command = commands[0]
    assert isinstance(command, BotArrivesAt), "bot arrived at"
    assert command.arrived_at == ends_at
