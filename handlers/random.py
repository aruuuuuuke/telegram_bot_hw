from aiogram import Router, types
from aiogram.filters import Command
import random

random_router = Router()

names = ["Aruuke", "Adinai","Sonia", "Maria"]

@random_router.message(Command("random"))
async def start_handler(message: types.Message):
    random_name = random.choice(names)
    await message.answer(f"Случайное имя: {random_name}")
