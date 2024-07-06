from aiogram.fsm.state import State, StatesGroup


class Questions(StatesGroup):
    FIRST = State()
    SECOND = State()
    THIRD = State()
    FOURTH = State()
    FIFTH = State()
    SIXTH = State()
    END = State()