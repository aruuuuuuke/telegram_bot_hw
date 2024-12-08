from aiogram.filters import Command
from aiogram import Router, types

from handlers.random_meal import dishes

start_router = Router()

list_id = []

@start_router.message(Command("start"))
async def start_handler(message: types.Message):
    name = message.from_user.first_name
    if message.from_user.id not in list_id:
        list_id.append(message.from_user.id)
    await message.answer(f"Hello {name},\nThere are {len(dishes)}, dishes in our cafe "
                         f"\nMy commands:"
                         f"\n/start - start working with bot"
                         f"\n/random_meal - random meal"
                         f"\n/menu - list of meals")
