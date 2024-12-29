from datetime import timedelta

from aiogram.filters import Command
from aiogram import Router, types, F

group_router = Router()
group_router.message.filter(F.chat.type != "private")

BAD_WORDS = ("дурак", "тупой", "гослинг", "арген")

@group_router.message(Command("ban"))
async def ban(message: types.Message):
    if not message.reply_to_message:
        await message.answer("Ваше сообщение должно быть ответом на чье то сообщение")
        return
    duration = timedelta(days=1)
    if "1д" in message.text:
        duration = timedelta(days=1)
    elif "3ч" in message.text:
        duration = timedelta(hours=3)
    elif "3н" in message.text:
        duration = timedelta(weeks=3)
    elif "10м" in message.text:
        duration = timedelta(minutes=10)
    until_date = message.date + duration
    await message.bot.ban_chat_member(
        chat_id=message.chat.id,
        user_id=message.reply_to_message.from_user.id,
        until_date=until_date,
    )
    await message.answer(f"Пользователь {message.reply_to_message.from_user.first_name} забанен")


@group_router.message()
async def group_handler(message: types.Message):
    lower_text = message.text.lower()
    for word in BAD_WORDS:
        if word in lower_text:
            await message.answer("Нельзя так говорить")
            await message.bot.ban_chat_member(
                chat_id=message.chat.id,
                user_id=message.from_user.id,
                # until_date=message.date + datetime.timedelta(seconds=180)
            )
            await message.answer("Бан на тебя")
            break
