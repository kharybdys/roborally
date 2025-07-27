# Architecture

## Goals
* All business logic is testable without Database connection
* Super coverage of tests in the business logic - all edge cases of the game rules as well
* "Onion" architecture
* Probably FastAPI and SQLAlchemy, still need to decide NoSQL vs SQL - this decision can be postponed
  until I'm done making the business logic

## Order of development
* Single bot movement
* Multi-bot movement
* Board movement
* Damage
* Repairing
* Movement Cards
* Board templates
* UI (for a single turn) - not showing the board
* UI (for a single turn) - showing the board before and after
* Event log after the turn
* Persistence
* UI for multiple turns
* CRUD UI (create game, list game)
* Auth
* Option cards (this is gonna be huge)

## Rough idea for now
* Game is a class that doesn't change state itself, it's a Mediator that just delegates.
* Board is a data model (probably Pydantic) that just contains the static board and its elements
  * Probably `dict[(x,y), Element]`
  * The elements don't persist coordinates and neighbours, that is probably a post_init on Board
  * Inheritance structure for the different types of board elements
* Bot is a data model
* Flag is a data model
* Separate calculation from data update, eg calculate what happens to a bot on movement (new coordinates, dies),
  return that as Command (Event/Action) class then have the Game execute the commands for the data updates.

## Open questions
* Game has players. Player has a bot (within the context of that game) and the game has those same bots.
  How to model?
