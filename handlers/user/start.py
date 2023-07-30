from aiogram import types
from keyboards.inline.menu_button import keyboard
from config.loader import bot
from handlers.user.commands_bot import set_starting_commands
#from data.text_data import LEVEL_LANG as td

async def start_bot(message: types.Message):
    await set_starting_commands(message.bot, message.from_user.id)
    await bot.send_message(
        chat_id=message.chat.id,
        text="Привет, я бот английского",
        reply_markup=keyboard
    )

# async def call_start(call: types.CallbackQuery):
#     action = call.data
#     if action == "lang":
#         await bot.send_message(chat_id=call.message.chat.id, text=td)
#     if action == "grammar":
#         await bot.send_message(chat_id=call.message.chat.id, )