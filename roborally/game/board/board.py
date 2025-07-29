import logging
from typing import Any

from pydantic import BaseModel, field_validator
from pydantic_core.core_schema import ValidatorFunctionWrapHandler

from roborally.game.board.coord import Coord
from roborally.game.board.elements.factory import BoardElements, DEFAULT_HOLE_ELEMENT
from roborally.game.direction import Direction

LOGGER = logging.getLogger(__name__)


class Board(BaseModel):
    elements: dict[Coord, BoardElements]

    def model_post_init(self, context: Any, /):
        for coords, element in self.elements.items():
            element._coords = coords
            for direction in Direction:
                other = direction.next_coords(coords)
                neighbour = self.element_at(other)
                element.add_neighbour(neighbour, direction)

    @field_validator("elements", mode="wrap")
    @classmethod
    def coerce_dict_keys(cls, value: Any, handler: ValidatorFunctionWrapHandler):
        if isinstance(value, dict):
            result = {}
            for key, item in value.items():
                if isinstance(key, str):
                    try:
                        new_key = Coord.model_validate_json(key)
                    except Exception as e:
                        LOGGER.warning(f"Problem transforming {key} to Coord", exc_info=e)
                        raise
                else:
                    new_key = key
                result[new_key] = item
            return handler(result)
        else:
            return handler(value)

    def element_at(self, coords: Coord) -> BoardElements:
        return self.elements.get(coords, DEFAULT_HOLE_ELEMENT)
