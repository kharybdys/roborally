from roborally.game.board.board import Board
from roborally.game.commands.base import BaseCommand
from roborally.game.commands.death import BotDies
from roborally.game.commands.movement import BotArrivesAt
from roborally.game.direction import Direction


def calculate_move(
    board: Board,
    start_x: int,
    start_y: int,
    movement_direction: Direction,
    steps: int,
) -> list[BaseCommand]:
    current_x, current_y = start_x, start_y
    for _ in range(steps):
        new_x, new_y = movement_direction.next_coords(current_x, current_y)
        board_element = board.element_at(new_x, new_y)
        if board_element.instant_death:
            return [BotDies(died_at_x=new_x, died_at_y=new_y)]
        current_x, current_y = new_x, new_y
    return [BotArrivesAt(new_x=current_x, new_y=current_y)]
