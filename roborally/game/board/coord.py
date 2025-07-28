import re
from typing import ClassVar, Self

from pydantic import BaseModel, ConfigDict


class Coord(BaseModel):
    model_config = ConfigDict(frozen=True)
    # This is how Coord gets dumped as a dict key by Pydantic, apparently
    _DICT_KEY_REGEX_PATTERN: ClassVar[re.Pattern] = re.compile(r"x=(?P<x>\d+) y=(?P<y>\d+)")

    x: int
    y: int

    def __eq__(self, other):
        if isinstance(other, Coord):
            return (self.x, self.y) == (other.x, other.y)
        return False

    def __hash__(self):
        return hash((self.x, self.y))

    @classmethod
    def parse_as_dict_key(cls, value: str) -> Self:
        if match := cls._DICT_KEY_REGEX_PATTERN.fullmatch(value):
            return cls(x=match.group("x"), y=match.group("y"))
        else:
            raise ValueError(f"Cannot parse {value} as a dict key for Coord")
