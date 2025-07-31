import logging

import pytest

from roborally.game.board.coord import Coord
from roborally.game.board.board import Board
from roborally.game.board.calculate_move import calculate_move
from roborally.game.commands.death import BotDies
from roborally.game.direction import Direction


LOGGER = logging.getLogger(__name__)


@pytest.mark.parametrize(
    ("start", "movement_direction", "steps", "death"),
    [
        # Will only just fall off the board
        (Coord(x=0, y=2), Direction.NORTH, 3, Coord(x=0, y=-1)),
        (Coord(x=1, y=1), Direction.NORTH, 2, Coord(x=1, y=-1)),
        (Coord(x=2, y=0), Direction.NORTH, 1, Coord(x=2, y=-1)),
        (Coord(x=0, y=0), Direction.EAST, 3, Coord(x=3, y=0)),
        (Coord(x=1, y=1), Direction.EAST, 2, Coord(x=3, y=1)),
        (Coord(x=2, y=2), Direction.EAST, 1, Coord(x=3, y=2)),
        (Coord(x=0, y=0), Direction.SOUTH, 3, Coord(x=0, y=3)),
        (Coord(x=1, y=1), Direction.SOUTH, 2, Coord(x=1, y=3)),
        (Coord(x=2, y=2), Direction.SOUTH, 1, Coord(x=2, y=3)),
        (Coord(x=2, y=0), Direction.WEST, 3, Coord(x=-1, y=0)),
        (Coord(x=1, y=1), Direction.WEST, 2, Coord(x=-1, y=1)),
        (Coord(x=0, y=2), Direction.WEST, 1, Coord(x=-1, y=2)),
        # Will very significantly fall of the board - verify died_at doesn't increase
        (Coord(x=0, y=0), Direction.NORTH, 2, Coord(x=0, y=-1)),
        (Coord(x=0, y=0), Direction.NORTH, 3, Coord(x=0, y=-1)),
        (Coord(x=0, y=0), Direction.NORTH, 4, Coord(x=0, y=-1)),
        (Coord(x=0, y=0), Direction.WEST, 2, Coord(x=-1, y=0)),
        (Coord(x=0, y=0), Direction.WEST, 3, Coord(x=-1, y=0)),
        (Coord(x=0, y=0), Direction.WEST, 4, Coord(x=-1, y=0)),
        (Coord(x=2, y=2), Direction.SOUTH, 2, Coord(x=2, y=3)),
        (Coord(x=2, y=2), Direction.SOUTH, 3, Coord(x=2, y=3)),
        (Coord(x=2, y=2), Direction.SOUTH, 4, Coord(x=2, y=3)),
        (Coord(x=2, y=2), Direction.EAST, 2, Coord(x=3, y=2)),
        (Coord(x=2, y=2), Direction.EAST, 3, Coord(x=3, y=2)),
        (Coord(x=2, y=2), Direction.EAST, 4, Coord(x=3, y=2)),
    ],
)
@pytest.mark.parametrize("board_name", ["three_by_three_empty_board"])
def test_falls_off_board(
    board: Board,
    start: Coord,
    movement_direction: Direction,
    steps: int,
    death: Coord,
):
    commands = calculate_move(
        board=board,
        start=start,
        movement_direction=movement_direction,
        steps=steps,
    )
    assert len(commands) == 1
    command = commands[0]
    assert isinstance(command, BotDies), "bot died"
    assert command.died_at == death


@pytest.mark.parametrize(
    ("start", "movement_direction", "steps", "death"),
    [
        (Coord(x=1, y=2), Direction.NORTH, 2, Coord(x=1, y=1)),
        (Coord(x=1, y=2), Direction.NORTH, 1, Coord(x=1, y=1)),
        (Coord(x=0, y=1), Direction.EAST, 2, Coord(x=1, y=1)),
        (Coord(x=0, y=1), Direction.EAST, 1, Coord(x=1, y=1)),
        (Coord(x=1, y=0), Direction.SOUTH, 2, Coord(x=1, y=1)),
        (Coord(x=1, y=0), Direction.SOUTH, 1, Coord(x=1, y=1)),
        (Coord(x=2, y=1), Direction.WEST, 2, Coord(x=1, y=1)),
        (Coord(x=2, y=1), Direction.WEST, 1, Coord(x=1, y=1)),
    ],
)
@pytest.mark.parametrize("board_name", ["three_by_three_with_hole_board"])
def test_falls_in_hole(
    board: Board,
    start: Coord,
    movement_direction: Direction,
    steps: int,
    death: Coord,
):
    commands = calculate_move(
        board=board,
        start=start,
        movement_direction=movement_direction,
        steps=steps,
    )
    assert len(commands) == 1
    command = commands[0]
    assert isinstance(command, BotDies), "bot died"
    assert command.died_at == death
