import asyncio
import logging
from bot_config import  dp,bot, database
from handlers import private_router
from handlers.group import group_router

async def on_startup(bot):
    database.create_table()

async def main():
    dp.include_router(private_router)
    dp.include_router(group_router)

    dp.startup.register(on_startup)

    await dp.start_polling(bot)

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())