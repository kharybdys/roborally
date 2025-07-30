import logging
from typing import Any, Self

from pydantic import BaseModel, field_validator, ConfigDict, model_validator
from pydantic_core.core_schema import ValidatorFunctionWrapHandler

from roborally.game.board.coord import Coord
from roborally.game.board.elements.factory import BoardElements
from roborally.game.board.elements.base import DEFAULT_HOLE_ELEMENT
from roborally.game.direction import Direction

LOGGER = logging.getLogger(__name__)


class Board(BaseModel):
    model_config = ConfigDict(frozen=True)

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

    @model_validator(mode="after")
    def check_walls_reciprocate(self) -> Self:
        for coord, element in self.elements.items():
            for wall_direction in element.walls:
                neighbour = element.get_neighbour(wall_direction)
                if not neighbour.instant_death and wall_direction.opposite not in neighbour.walls:
                    raise ValueError(f"Wall in direction {wall_direction} on coordinates {coord} does not reciprocate")
        return self

    def element_at(self, coords: Coord) -> BoardElements:
        return self.elements.get(coords, DEFAULT_HOLE_ELEMENT)
