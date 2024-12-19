from aiogram import Router, types, F
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext
from bot_config import database

list_user=[]


otzyv_router = Router()

class RestourantReview(StatesGroup):
    name = State()
    instagram_username = State()
    food_rating = State()
    visit_date = State()
    cleanliness_rating = State()
    extra_comments = State()

@otzyv_router.callback_query(F.data == "review")
async def start(callback: types.CallbackQuery, state: FSMContext):
    if callback.from_user.id in list_user:
        await callback.message.answer("Вы уже оставляли отзыв")
    else:
        await callback.message.answer("Как вас зовут?")
        await state.set_state(RestourantReview.name)

@otzyv_router.message(RestourantReview.name)
async def ask_instagram(message: types.Message, state: FSMContext):
    name = message.text
    if len(name) > 20 or len(name) < 3:
        await message.answer("Введите коректное имя")
        return
    await state.update_data(name=message.text)
    await message.answer(f"{message.text}, Какой ваш Instagram аккаунт?")
    await state.set_state(RestourantReview.visit_date)

@otzyv_router.message(RestourantReview.visit_date)
async def ask_visit_date(message: types.Message, state: FSMContext):
    await state.update_data(instagram_username=message.text)
    await message.answer(f"когда вы посещали наше заведение?")
    await state.set_state(RestourantReview.instagram_username)

@otzyv_router.message(RestourantReview.instagram_username)
async def ask_food_rating(message: types.Message, state: FSMContext):
    kb = types.ReplyKeyboardMarkup(
        keyboard=[
            [
                types.KeyboardButton(text="1"),
                types.KeyboardButton(text="2"),
                types.KeyboardButton(text="3"),
                types.KeyboardButton(text="4"),
                types.KeyboardButton(text="5"),
            ],
        ],
        resize_keyboard = True,
        input_field_placeholder = "Оцените еду"
    )
    await state.update_data(visit_date=message.text)
    await message.answer("Как оцениваете качество еды?", reply_markup=kb)
    await state.set_state(RestourantReview.food_rating)


@otzyv_router.message(RestourantReview.food_rating)
async def ask_cleanliness_rating(message: types.Message, state: FSMContext):
    kb = types.ReplyKeyboardMarkup(
        keyboard=[
            [
                types.KeyboardButton(text="1"),
                types.KeyboardButton(text="2"),
                types.KeyboardButton(text="3"),
                types.KeyboardButton(text="4"),
                types.KeyboardButton(text="5"),
            ],
        ],
        resize_keyboard = True,
        input_field_placeholder = "Оцените чистоту"
    )
    await state.update_data(food_rating = message.text)
    await message.answer("Как оцениваете чистоту помещения?", reply_markup=kb)
    await state.set_state(RestourantReview.cleanliness_rating)

@otzyv_router.message(RestourantReview.cleanliness_rating)
async def ask_extra_comments(message: types.Message, state: FSMContext):
    await state.update_data(cleanliness_rating=message.text)
    kb = types.InlineKeyboardMarkup(
        inline_keyboard=[
            [
                types.InlineKeyboardButton(text="Да", callback_data="yes"),
                types.InlineKeyboardButton(text="Нет", callback_data="no")
            ],
        ]
    )
    await message.answer("Есть ли у вас дополнительные комментарии или жалобы?", reply_markup = kb)
    await state.set_state(RestourantReview.extra_comments)

@otzyv_router.callback_query(F.data == "yes")
async def ask_for_comment(callback: types.CallbackQuery, state: FSMContext):
    await callback.message.answer("Пожалуйста, оставьте ваш комментарий.")
    await state.set_state(RestourantReview.extra_comments)


@otzyv_router.callback_query(F.data == "no")
async def skip_comment(callback: types.CallbackQuery, state: FSMContext):
    data = await state.get_data()
    review = (
        f"Спасибо за ваш отзыв!\n"
        f"Имя: {data['name']}\n"
        f"Instagram: {data['instagram_username']}\n"
        f"Оценка качества еды: {data['food_rating']}\n"
        f"Оценка чистоты: {data['cleanliness_rating']}\n"
        f"Дополнительные комментарии: Нет комментариев"
    )
    await callback.message.answer(review)

@otzyv_router.message(RestourantReview.extra_comments)
async def finish_review(message: types.Message, state: FSMContext):
    list_user.append(message.from_user.id)
    data = await state.get_data()
    review = (
        f"Спасибо за ваш отзыв!\n"
        f"Имя: {data['name']}\n"
        f"Instagram: {data['instagram_username']}\n"
        f"Дата посещения: {data['visit_date']}\n"
        f"Оценка качества еды: {data['food_rating']}\n"
        f"Оценка чистоты: {data['cleanliness_rating']}\n"
        f"Дополнительные комментарии: {message.text}"
    )
    await message.answer(review)
    print(data)
    database.save_survey(data)
    await state.clear()

