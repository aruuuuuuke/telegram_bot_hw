from aiogram import Router, types
from aiogram.filters import Command
from bot_config import database
from pprint import pprint
# from handlers.random_meal import dishes

menu_router = Router()

@menu_router.message(Command("menu"))
async def start_handler(message: types.Message):
    meal_list = database.get_meals_by_price()
    pprint(meal_list)
    for meal in meal_list:
        txt = (f"Название: {meal['name']}\n"
               f"Цена: {meal['price']}")
        await message.answer(txt)

# async def start_handler(message: types.Message):
#     meal_list = database.get_all_meals()
#     pprint(meal_list)
#     for meal in meal_list:
#         txt = (f"Название: {meal['name']}\n"
#                f"Цена: {meal['price']}")
#         await message.answer(txt)

