from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

keyboard = InlineKeyboardMarkup()
start_test = InlineKeyboardButton(text="Пройти тест на тему 'Артикли a/an, the'", callback_data="start_test2")
keyboard.add(start_test)