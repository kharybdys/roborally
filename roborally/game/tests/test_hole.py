import pytest

from roborally.game.board.coord import Coord
from roborally.game.board.elements.base import EmptyElement
from roborally.game.board.board import Board
from roborally.game.board.calculate_move import calculate_move
from roborally.game.commands.death import BotDies
from roborally.game.direction import Direction


# TODO: Solve that model_dump_json doesn't provide output that can be model_validated
@pytest.fixture
def three_by_three_empty_board_json(data_dir) -> Board:
    with open(data_dir / "three_by_three_empty_board.json") as f:
        board = Board.model_validate_json(f.read())
    return board


@pytest.fixture
def three_by_three_empty_board(data_dir) -> Board:
    result = Board(
        elements={
            Coord(x=0, y=0): EmptyElement(),
            Coord(x=0, y=1): EmptyElement(),
            Coord(x=0, y=2): EmptyElement(),
            Coord(x=1, y=0): EmptyElement(),
            Coord(x=1, y=1): EmptyElement(),
            Coord(x=1, y=2): EmptyElement(),
            Coord(x=2, y=0): EmptyElement(),
            Coord(x=2, y=1): EmptyElement(),
            Coord(x=2, y=2): EmptyElement(),
        }
    )
    print(result.model_dump_json(round_trip=True))
    return result


@pytest.mark.parametrize(
    ("start", "movement_direction", "steps", "death"),
    [
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
    ],
)
def test_falls_in_hole(
    three_by_three_empty_board: Board,
    start: Coord,
    movement_direction: Direction,
    steps: int,
    death: Coord,
):
    commands = calculate_move(
        board=three_by_three_empty_board,
        start=start,
        movement_direction=movement_direction,
        steps=steps,
    )
    assert len(commands) == 1
    assert isinstance(commands[0], BotDies), "bot died"
    assert commands[0].died_at == death
