from typing import Literal

from roborally.game.board.elements.base import BaseElement


class Pusher135(BaseElement):
    discriminator: Literal["PUSHER_135"] = "PUSHER_135"


class Pusher24(BaseElement):
    discriminator: Literal["PUSHER_24"] = "PUSHER_24"
