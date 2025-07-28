from roborally.game.board.board import Board
from roborally.game.board.coord import Coord
from roborally.game.commands.base import BaseCommand
from roborally.game.commands.death import BotDies
from roborally.game.commands.movement import BotArrivesAt
from roborally.game.direction import Direction


def calculate_move(
    board: Board,
    start: Coord,
    movement_direction: Direction,
    steps: int,
) -> list[BaseCommand]:
    current = start
    for _ in range(steps):
        new_coords = movement_direction.next_coords(current)
        board_element = board.element_at(new_coords)
        if board_element.instant_death:
            return [BotDies(died_at=new_coords)]
        current = new_coords
    return [BotArrivesAt(arrived_at=current)]
