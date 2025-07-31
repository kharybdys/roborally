from roborally.game.board.board import Board
from roborally.game.board.coord import Coord
from roborally.game.commands.base import BaseCommand
from roborally.game.commands.death import BotDies
from roborally.game.commands.movement import BotArrivesAt, BotHitsWall
from roborally.game.direction import Direction


def calculate_move(
    board: Board,
    start: Coord,
    movement_direction: Direction,
    steps: int,
) -> list[BaseCommand]:
    # Handle negative steps by adjusting our parameters:
    if steps < 0:
        return calculate_move(
            board=board,
            start=start,
            movement_direction=movement_direction.opposite,
            steps=-1 * steps,
        )

    current = start

    for _ in range(steps):
        current_board_element = board.element_at(current)
        if movement_direction in current_board_element.walls:
            return [BotHitsWall(wall_at=current, wall_direction=movement_direction), BotArrivesAt(arrived_at=current)]

        new_coords = movement_direction.next_coords(current)
        new_board_element = board.element_at(new_coords)
        if new_board_element.instant_death:
            return [BotDies(died_at=new_coords)]

        current = new_coords

    return [BotArrivesAt(arrived_at=current)]
