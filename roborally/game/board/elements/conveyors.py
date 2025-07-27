from typing import Literal

from roborally.game.board.elements.base import BaseElement


class ConveyorSingleSpeed(BaseElement):
    discriminator: Literal["CONVEYOR_SINGLE_SPEED"] = "CONVEYOR_SINGLE_SPEED"


class ConveyorDoubleSpeed(BaseElement):
    discriminator: Literal["CONVEYOR_DOUBLE_SPEED"] = "CONVEYOR_DOUBLE_SPEED"
