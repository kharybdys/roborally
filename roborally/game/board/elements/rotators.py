from typing import Literal

from roborally.game.board.elements.base import BaseElement


class RotatorClockwise(BaseElement):
    discriminator: Literal["ROTATOR_CLOCKWISE"] = "ROTATOR_CLOCKWISE"


class RotatorCounterClockwise(BaseElement):
    discriminator: Literal["ROTATOR_COUNTERCLOCKWISE"] = "ROTATOR_COUNTERCLOCKWISE"
