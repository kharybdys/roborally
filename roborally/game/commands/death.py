from roborally.game.board.coord import Coord
from roborally.game.commands.base import BaseCommand


class BotDies(BaseCommand):
    died_at: Coord

    def process(self):
        pass
