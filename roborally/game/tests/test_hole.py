import pytest

from roborally.game.board.board import Board
from roborally.game.board.calculate_move import calculate_move
from roborally.game.commands.death import BotDies
from roborally.game.direction import Direction


@pytest.fixture
def three_by_three_empty_board(data_dir) -> Board:
    with open(data_dir / "three_by_three_empty_board.json") as f:
        board = Board.model_validate_json(f.read())
    return board


@pytest.mark.parametrize(
    ("start_x", "start_y", "movement_direction", "steps", "death_x", "death_y"),
    [
        (0, 2, Direction.NORTH, 3, 0, -1),
        (1, 1, Direction.NORTH, 2, 1, -1),
        (2, 0, Direction.NORTH, 1, 2, -1),
        (0, 0, Direction.EAST, 3, 3, 0),
        (1, 1, Direction.EAST, 2, 3, 1),
        (2, 2, Direction.EAST, 1, 3, 2),
        (0, 0, Direction.SOUTH, 3, 0, 3),
        (1, 1, Direction.SOUTH, 2, 1, 3),
        (2, 2, Direction.SOUTH, 1, 2, 3),
        (2, 0, Direction.WEST, 3, -1, 0),
        (1, 1, Direction.WEST, 2, -1, 1),
        (0, 2, Direction.WEST, 1, -1, 2),
    ],
)
def test_falls_in_hole(
    three_by_three_empty_board: Board,
    start_x: int,
    start_y: int,
    movement_direction: Direction,
    steps: int,
    death_x: int,
    death_y: int,
):
    commands = calculate_move(
        board=three_by_three_empty_board,
        start_x=start_x,
        start_y=start_y,
        movement_direction=movement_direction,
        steps=steps,
    )
    assert len(commands) == 1
    assert isinstance(commands[0], BotDies)
    assert commands[0].died_at_x == death_x
    assert commands[0].died_at_y == death_y
