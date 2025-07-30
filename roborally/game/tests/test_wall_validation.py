from pathlib import Path

import pytest
from pydantic import ValidationError

from roborally.game.board.board import Board


@pytest.mark.parametrize(
    ("board_name", "wall_count"),
    [
        ("wall_validation/valid_walls", 4),
        ("wall_validation/valid_walls_outside", 12),
        ("wall_validation/valid_walls_with_hole", 8),
    ],
)
def test_board_with_valid_walls(data_dir: Path, board_name: str, wall_count: int):
    # Just needs to load without error
    with open(data_dir / f"{board_name}.json") as f:
        board = Board.model_validate_json(f.read())

    actual_wall_count = sum(len(element.walls) for element in board.elements.values())
    assert actual_wall_count == wall_count


@pytest.mark.parametrize(
    "board_name",
    [
        "wall_validation/invalid_walls",
    ],
)
def test_board_with_invalid_walls(data_dir: Path, board_name: str):
    with pytest.raises(
        ValidationError, match='Wall in direction Direction.NORTH on coordinates {"x":0,"y":1} does not reciprocate'
    ):
        with open(data_dir / f"{board_name}.json") as f:
            Board.model_validate_json(f.read())
