from aiogram import Router, types, F
from aiogram.filters import Command
from aiogram.types import ContentType
from aiogram import Router, types, F
from aiogram.filters import Command
from aiogram.fsm.state import State, StatesGroup, default_state
from aiogram.fsm.context import FSMContext
from bot_config import database
from pprint import pprint

admin_router = Router()
admin_router.message.filter(F.from_user.id == 5553751043)
admin_router.callback_query.filter(F.from_user.id == 5553751043)


class Meal(StatesGroup):
    name = State()
    price = State()
    photo = State()
    receipt = State()
    category = State()



@admin_router.message(Command("stop"))
@admin_router.message(F.text == "стоп")
async def stop(message: types.Message, state: FSMContext):
    await state.clear()
    await message.answer("Опрос отсановлен")

@admin_router.message(Command("new_meal"), default_state)
async def name_meal(message: types.Message, state: FSMContext):
    await message.answer("Введите название блюда")
    await state.set_state(Meal.name)


@admin_router.message(Meal.name)
async def price_meal(message: types.Message, state: FSMContext):
    await state.update_data(name=message.text)
    await message.answer("Введите цену блюда")
    await state.set_state(Meal.price)

@admin_router.message(Meal.price)
async def meal_photo(message: types.Message, state: FSMContext):
    await state.update_data(price=message.text)
    await message.answer("Загрузите фото блюда")
    await state.set_state(Meal.photo)


@admin_router.message(Meal.photo)
async def set_reciept(message: types.Message, state: FSMContext):
    meal_photo = message.photo
    pprint(meal_photo)
    biggest_image = meal_photo[-1]
    biggest_image_id = biggest_image.file_id
    await state.update_data(photo=biggest_image_id)
    await message.answer("Введиет рецепт/описание блюда")
    await state.set_state(Meal.receipt)


@admin_router.message(Meal.receipt)
async def set_cotegory(message: types.Message, state: FSMContext):
    kb = types.ReplyKeyboardMarkup(
        keyboard = [
            [
                types.KeyboardButton(text ="Супы"),
                types.KeyboardButton(text ="Вторые")
            ],
            [
                types.KeyboardButton(text="Горячие"),
                types.KeyboardButton(text="Напитки")
            ],
        ],
        resize_keyboard = True,
        input_field_placeholder = "Выберите категорию"
    )
    await state.update_data(reciept=message.text)
    await message.answer("Выберите категорию вашего блюда", reply_markup=kb)
    await state.set_state(Meal.category)

@admin_router.message(Meal.category)
async def create_new_book(message: types.Message, state: FSMContext):
    await state.update_data(category=message.text)
    data = await state.get_data()
    print(data)
    database.save_meal(data)
    await message.answer("Блюдо сохранено")
    await state.clear()


