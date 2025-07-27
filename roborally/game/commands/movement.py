from roborally.game.commands.base import BaseCommand


class BotArrivesAt(BaseCommand):
    new_x: int
    new_y: int

    def process(self):
        pass
