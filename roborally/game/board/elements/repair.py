from typing import Literal

from roborally.game.board.elements.base import BaseElement


class Repair(BaseElement):
    discriminator: Literal["REPAIR"] = "REPAIR"


class RepairAndOption(BaseElement):
    discriminator: Literal["REPAIR_AND_OPTION"] = "REPAIR_AND_OPTION"
