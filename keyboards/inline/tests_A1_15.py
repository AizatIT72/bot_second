from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

keyboard = InlineKeyboardMarkup()
start_test = InlineKeyboardButton(text="Пройти тест на тему 'Present Continuous'", callback_data="start_test15")
keyboard.add(start_test)