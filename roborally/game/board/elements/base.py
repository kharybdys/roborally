from typing import Literal, Self

from pydantic import BaseModel

from roborally.game.board.coord import Coord
from roborally.game.direction import Direction


class BaseElement(BaseModel):
    discriminator: str
    _coords: Coord = Coord(x=-1, y=-1)
    _neighbours: dict[Direction, Self] = {}

    def add_neighbour(self, neighbour: Self, direction: Direction):
        self._neighbours[direction] = neighbour

    @property
    def instant_death(self) -> bool:
        return False


class EmptyElement(BaseElement):
    discriminator: Literal["EMPTY"] = "EMPTY"


class Hole(BaseElement):
    discriminator: Literal["HOLE"] = "HOLE"

    @property
    def instant_death(self) -> bool:
        return True
