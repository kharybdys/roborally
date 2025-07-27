from roborally.game.commands.base import BaseCommand


class BotDies(BaseCommand):
    died_at_x: int
    died_at_y: int

    def process(self):
        pass
