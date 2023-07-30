from aiogram import types
from config.loader import bot
from data.text_data import LEVEL_LANG as td
from keyboards.inline.grammar_level import keyboard

async def call_start(call: types.CallbackQuery):
    action = call.data
    # if action == "lang":
    #     await bot.send_message(chat_id=call.message.chat.id, text=td)
    await bot.send_message(chat_id=call.message.chat.id,
                           text="Выберите свой подходящий уровень для продолжения изучения грамматики",
                           reply_markup=keyboard)

#callback_data = "a1"
async def lang_func(call: types.CallbackQuery):
    await bot.send_message(chat_id=call.message.chat.id, text=td)
