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

    # This determines how Coord looks like as dict key in a model dump action
    def __str__(self):
        return self.model_dump_json()
