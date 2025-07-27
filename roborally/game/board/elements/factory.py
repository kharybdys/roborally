from typing import TypeAlias, Annotated

from pydantic import Discriminator

from roborally.game.board.elements.base import EmptyElement, Hole
from roborally.game.board.elements.conveyors import ConveyorSingleSpeed, ConveyorDoubleSpeed
from roborally.game.board.elements.pushers import Pusher135, Pusher24
from roborally.game.board.elements.repair import Repair, RepairAndOption
from roborally.game.board.elements.rotators import RotatorClockwise, RotatorCounterClockwise

BoardElements: TypeAlias = Annotated[
    EmptyElement
    | Hole
    | RotatorClockwise
    | RotatorCounterClockwise
    | Pusher135
    | Pusher24
    | ConveyorSingleSpeed
    | ConveyorDoubleSpeed
    | Repair
    | RepairAndOption,
    Discriminator("discriminator"),
]
DEFAULT_HOLE_ELEMENT = Hole()
