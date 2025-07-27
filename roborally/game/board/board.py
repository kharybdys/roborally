from typing import Any

from pydantic import BaseModel

from roborally.game.board.coord import Coord
from roborally.game.board.elements.factory import BoardElements, DEFAULT_HOLE_ELEMENT
from roborally.game.direction import Direction


class Board(BaseModel):
    elements: dict[Coord, BoardElements]

    def model_post_init(self, context: Any, /):
        for coords, element in self.elements.items():
            element._coords = coords
            for direction in Direction:
                other = direction.next_coords(coords)
                neighbour = self.element_at(other)
                element.add_neighbour(neighbour, direction)

    def element_at(self, coords: Coord) -> BoardElements:
        return self.elements.get(coords, DEFAULT_HOLE_ELEMENT)
