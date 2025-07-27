from enum import Enum
from typing import Self

from roborally.game.board.coord import Coord


class Direction(Enum):
    NORTH = "NORTH"
    EAST = "EAST"
    SOUTH = "SOUTH"
    WEST = "WEST"

    @classmethod
    def turn_order(cls) -> list[Self]:
        return [cls.NORTH, cls.EAST, cls.SOUTH, cls.WEST]

    def turn_clockwise(self, turns: int) -> Self:
        if turns > 4 or turns < -4:
            raise ValueError(f"Turns value outside [-4, 4] not supported, got {turns}")
        turn_order = self.turn_order()
        my_idx = turn_order.index(self)
        new_idx = (my_idx + turns) % len(turn_order)
        return turn_order[new_idx]

    def next_coords(self, current: Coord) -> Coord:
        """Returns the resulting coordinates if we would make one step in direction (self) given x, y as start coordinates."""
        match self:
            case Direction.WEST:
                return Coord(x=current.x - 1, y=current.y)
            case Direction.EAST:
                return Coord(x=current.x + 1, y=current.y)
            case Direction.NORTH:
                return Coord(x=current.x, y=current.y - 1)
            case Direction.SOUTH:
                return Coord(x=current.x, y=current.y + 1)
            case _:
                raise ValueError(f"Unsupported direction {self}")
