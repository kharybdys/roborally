from pathlib import Path

import pytest

from roborally.game.board.board import Board


@pytest.fixture
def data_dir() -> Path:
    return Path(__file__).parent / "data"


@pytest.fixture
def board(data_dir: Path, board_name: str) -> Board:
    with open(data_dir / f"{board_name}.json") as f:
        board = Board.model_validate_json(f.read())
    return board
