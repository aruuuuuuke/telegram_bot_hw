import asyncio
import logging
from bot_config import bot, dp
from handlers.start import start_router
from handlers.menu import menu_router
from handlers.random import random_router
from handlers.random_meal import random_meal_router
from handlers.other_messages import echo_handlr

async def main():
    dp.include_router(start_router)
    dp.include_router(menu_router)
    dp.include_router(random_router)
    dp.include_router(random_meal_router)
    dp.include_router(echo_handlr)
    await dp.start_polling(bot)

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())