from aiogram import types
from config.loader import bot
import random
from aiogram.dispatcher import FSMContext
from states.games import Game
from config.loader import dp

word_image_pairs = {
    "apple": "https://cdn.food.ru/unsigned/fit/640/480/ce/0/czM6Ly9tZWRpYS9waWN0dXJlcy8yMDIxMTEyNi8zODdwbnQuanBlZw.jpg",
    "banana": "https://static.wikia.nocookie.net/fnaf-fanon-animatronics/images/4/40/%D0%91%D0%B0%D0%BD%D0%B0%D0%BD.png/revision/latest?cb=20190614113143&path-prefix=ru",
    "cucumber": "https://calorizator.ru/sites/default/files/imagecache/product_512/product/cucumber-1.jpg"
}

USERS_STATE = {}


async def start_game(message: types.Message, state: FSMContext):
    await Game().stage_game.set()



async def check_answer(message: types.Message):
    user_id = message.from_user.id
    user_answer = message.text.strip().lower()
    if user_id not in USERS_STATE:
        await message.reply("Чтобы начать игру, используйте команду /start_game")
        return
    current_word = USERS_STATE[user_id]["current_word"]
    if user_answer == current_word:
        await message.reply("Правильно! Вы угадали слово.")
    else:
        await message.reply("Неправильно. Попробуйте еще раз.")
    del USERS_STATE[user_id]
    #await state.finish()