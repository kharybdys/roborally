from pydantic import BaseModel, ConfigDict


class Coord(BaseModel):
    model_config = ConfigDict(frozen=True)

    x: int
    y: int

    def __eq__(self, other):
        if isinstance(other, Coord):
            return (self.x, self.y) == (other.x, other.y)
        return False

    def __hash__(self):
        return hash((self.x, self.y))
