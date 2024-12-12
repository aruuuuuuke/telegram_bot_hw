from aiogram import Router, types

echo_handlr = Router()

@echo_handlr.message()
async def echo_handler(message: types.Message):
    txt = message.text
    await message.answer(txt)