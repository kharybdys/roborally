from enum import Enum
from typing import Self


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
