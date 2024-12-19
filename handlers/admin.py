from aiogram import Router, types, F
from aiogram.filters import Command
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext
from bot_config import dp

admin_router = Router()
admin_router.message.filter(F.from_user.id == 5553751043)
admin_router.callback_query.filter(F.from_user.id == 5553751043)


class Meal(StatesGroup):
    name = State()
    price = State()
    genre = State()