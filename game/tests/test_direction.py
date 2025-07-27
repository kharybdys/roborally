import pytest as pytest

from game.direction import Direction


@pytest.mark.parametrize(
    ("initial_direction", "turns", "expected_direction"),
    [
        (Direction.NORTH, -4, Direction.NORTH),
        (Direction.NORTH, -3, Direction.EAST),
        (Direction.NORTH, -2, Direction.SOUTH),
        (Direction.NORTH, -1, Direction.WEST),
        (Direction.NORTH, 0, Direction.NORTH),
        (Direction.NORTH, 1, Direction.EAST),
        (Direction.NORTH, 2, Direction.SOUTH),
        (Direction.NORTH, 3, Direction.WEST),
        (Direction.NORTH, 4, Direction.NORTH),
        (Direction.EAST, -4, Direction.EAST),
        (Direction.EAST, -3, Direction.SOUTH),
        (Direction.EAST, -2, Direction.WEST),
        (Direction.EAST, -1, Direction.NORTH),
        (Direction.EAST, 0, Direction.EAST),
        (Direction.EAST, 1, Direction.SOUTH),
        (Direction.EAST, 2, Direction.WEST),
        (Direction.EAST, 3, Direction.NORTH),
        (Direction.EAST, 4, Direction.EAST),
        (Direction.SOUTH, -4, Direction.SOUTH),
        (Direction.SOUTH, -3, Direction.WEST),
        (Direction.SOUTH, -2, Direction.NORTH),
        (Direction.SOUTH, -1, Direction.EAST),
        (Direction.SOUTH, 0, Direction.SOUTH),
        (Direction.SOUTH, 1, Direction.WEST),
        (Direction.SOUTH, 2, Direction.NORTH),
        (Direction.SOUTH, 3, Direction.EAST),
        (Direction.SOUTH, 4, Direction.SOUTH),
        (Direction.WEST, -4, Direction.WEST),
        (Direction.WEST, -3, Direction.NORTH),
        (Direction.WEST, -2, Direction.EAST),
        (Direction.WEST, -1, Direction.SOUTH),
        (Direction.WEST, 0, Direction.WEST),
        (Direction.WEST, 1, Direction.NORTH),
        (Direction.WEST, 2, Direction.EAST),
        (Direction.WEST, 3, Direction.SOUTH),
        (Direction.WEST, 4, Direction.WEST),
    ],
)
def test_direction(initial_direction: Direction, turns: int, expected_direction: Direction):
    output_direction = initial_direction.turn_clockwise(turns)
    assert output_direction == expected_direction


@pytest.mark.parametrize(
    ("turns",),
    [
        (-8,),
        (-7,),
        (-6,),
        (-5,),
        (5,),
        (6,),
        (7,),
        (8,),
    ],
)
def test_direction_invalid_turns(turns: int):
    for initial_direction in Direction:
        with pytest.raises(ValueError, match="not supported"):
            initial_direction.turn_clockwise(turns)
