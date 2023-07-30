from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

keyboard = InlineKeyboardMarkup()
start_test = InlineKeyboardButton(text="Пройти тест на тему 'Единственное и множественное число существительных (-s, -es)'", callback_data="start_test5")
keyboard.add(start_test)