from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

keyboard = InlineKeyboardMarkup()
start_test = InlineKeyboardButton(text="Пройти тест на тему 'Вопросы с what, who, where, when, why, how, how much (many)'", callback_data="start_test4")
keyboard.add(start_test)