from aiogram import Router, types
from aiogram.filters import Command
import random

random_meal_router = Router()

dishes = [
    {
        "name": "Паста Карбонара",
        "recipe": "Оригинальный итальянский рецепт: аппетитная паста, приготовленная с хрустящим беконом, "
                  "деликатным соусом из свежих яиц и пармезана, приправленная ароматным черным перцем. "
                  "Подаётся с легкой кремовой текстурой, идеальной для гурманов.",
        "photo": "images/Pasta.jpg"
    },
    {
        "name": "Цезарь",
        "recipe": "Легендарный салат, где хрустящие листья ромен сочетаются с нежными кусочками обжаренной курицы, "
                  "золотистыми крутонами и пармезаном. Традиционная заправка Цезарь придает блюду насыщенный вкус, "
                  "который невозможно забыть.",
        "photo": "images/cezar.jpg"
    },
    {
        "name": "Борщ",
        "recipe": "Классический борщ с богатым и насыщенным вкусом: нежное мясо, свежие овощи, свекла и капуста, "
                  "приправленные ароматными специями. Подаётся горячим с ложкой сметаны и зеленью для идеального акцента.",
        "photo": "images/borsh.jpg"
    }
]


@random_meal_router.message(Command("random_meal"))
async def start_handler(message: types.Message):
    random_meal = random.choice(dishes)
    photo = types.FSInputFile(f"{random_meal['photo']}")
    await message.answer_photo(photo= photo,
                               caption = f"{random_meal['name']}"
                                         f"\n{random_meal['recipe']}")