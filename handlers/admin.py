from aiogram import Router, types, F
from aiogram.filters import Command
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext
from bot_config import database

admin_router = Router()
admin_router.message.filter(F.from_user.id == 5553751043)
admin_router.callback_query.filter(F.from_user.id == 5553751043)


class Meal(StatesGroup):
    name = State()
    price = State()
    receipt = State()
    category = State()
    # photo = State()


@admin_router.message(Command("new_meal"))
async def name_meal(message: types.Message, state: FSMContext):
    await message.answer("Введите название блюда")
    await state.set_state(Meal.name)


@admin_router.message(Meal.name)
async def price_meal(message: types.Message, state: FSMContext):
    await state.update_data(name=message.text)
    await message.answer("Введите цену блюда")
    await state.set_state(Meal.price)


@admin_router.message(Meal.price)
async def ser_reciept(message: types.Message, state: FSMContext):
    await state.update_data(price=message.text)
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

# async def ser_photo(message: types.Message, state: FSMContext):
#     await state.update_data(category=message.text)
#     await message.answer("Отправьте фото вашего блюда")
#     await state.set_state(Meal.receipt)

