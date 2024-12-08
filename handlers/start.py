from aiogram.filters import Command
from aiogram import Router, types

start_router = Router()

list_id = []

@start_router.message(Command("start"))
async def start_handler(message: types.Message):
    name = message.from_user.first_name
    if message.from_user.id not in list_id:
        list_id.append(message.from_user.id)
    await message.answer(f"Hello {name},\nour bot is serving {len(list_id)}, people "
                         f"\nMy commands:"
                         f"\n/start - start working with bot"
                         f"\n/random - random name"
                         f"\n/myinfo - information of user")
