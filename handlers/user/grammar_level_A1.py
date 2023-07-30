from aiogram import types
from config.loader import bot
from keyboards.inline.grammar_topic import keyboard

#Уровень А1 - Список тем
async def gramm1(call: types.CallbackQuery):
    # action = call.data
    await bot.send_message(chat_id=call.message.chat.id, text="Список тем", reply_markup=keyboard)