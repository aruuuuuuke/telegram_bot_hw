import asyncio
import random
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from dotenv import dotenv_values

token = dotenv_values(".env")["BOT_TOKEN"]
bot = Bot(token = token)
dp = Dispatcher()

list_id = []


@dp.message(Command("start"))
async def start_handler(message: types.Message):
    name = message.from_user.first_name
    if message.from_user.id not in list_id:
        list_id.append(message.from_user.id)
    await message.answer(f"Hello {name}, our bot is serving {len(list_id)}, people")


@dp.message(Command("myinfo"))
async def start_handler(message: types.Message):
    id = message.from_user.id
    name = message.from_user.first_name
    username = message.from_user.username
    await message.answer(f"Your id: {id}\nName: {name}\nUsername: {username}")

names = ["Aruuke", "Adinai","Sonia", "Maria"]

@dp.message(Command("random"))
async def start_handler(message: types.Message):
    random_name = random.choice(names)
    await message.answer(f"Случайное имя: {random_name}")


@dp.message()
async def echo_handler(message: types.Message):
    txt = message.text
    await message.answer(txt)



async def main():
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())