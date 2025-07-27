from typing import Any

from pydantic import BaseModel

from roborally.game.board.elements.factory import BoardElements, DEFAULT_HOLE_ELEMENT
from roborally.game.direction import Direction


class Board(BaseModel):
    elements: dict[tuple[int, int], BoardElements]

    def model_post_init(self, context: Any, /):
        for (x, y), element in self.elements.items():
            element._x = x
            element._y = y
            for direction in Direction:
                other_x, other_y = direction.next_coords(x, y)
                neighbour = self.element_at(other_x, other_y)
                element.add_neighbour(neighbour, direction)

    def element_at(self, x: int, y: int) -> BoardElements:
        return self.elements.get((x, y), DEFAULT_HOLE_ELEMENT)
