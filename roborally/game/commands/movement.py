from roborally.game.board.coord import Coord
from roborally.game.commands.base import BaseCommand
from roborally.game.direction import Direction


class BotHitsWall(BaseCommand):
    wall_at: Coord
    wall_direction: Direction

    def process(self):
        pass


class BotArrivesAt(BaseCommand):
    arrived_at: Coord

    def process(self):
        pass
