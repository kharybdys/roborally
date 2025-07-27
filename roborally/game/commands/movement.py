from roborally.game.board.coord import Coord
from roborally.game.commands.base import BaseCommand


class BotArrivesAt(BaseCommand):
    new: Coord

    def process(self):
        pass
