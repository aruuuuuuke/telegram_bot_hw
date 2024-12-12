from aiogram import Router, types
from aiogram.filters import Command

from handlers.random_meal import dishes

menu_router = Router()

@menu_router.message(Command("menu"))
async def start_handler(message: types.Message):
    # id = message.from_user.id
    # name = message.from_user.first_name
    # username = message.from_user.username
    await message.answer(f"Cписок блюд:"
                         f"\n{dishes[0]['name']}"
                         f"\n{dishes[1]['name']}"
                         f"\n{dishes[2]['name']}")

