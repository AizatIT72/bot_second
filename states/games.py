from aiogram.dispatcher.filters.state import StatesGroup, State

class Game(StatesGroup):
    stage_game = State()