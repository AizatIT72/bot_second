from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

keyboard = InlineKeyboardMarkup()
start_test = InlineKeyboardButton(text="Пройти тест на тему 'There is/are'", callback_data="start_test3")
keyboard.add(start_test)