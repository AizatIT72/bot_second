from aiogram import types
from config.loader import bot
from keyboards.inline.reading import keyboard


async def read(call: types.CallbackQuery):
    await bot.send_message(chat_id=call.message.chat.id, text="Вот книги", reply_markup=keyboard)