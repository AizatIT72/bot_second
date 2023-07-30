from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

keyboard = InlineKeyboardMarkup()
start_test = InlineKeyboardButton(text="Пройти тест на тему 'Неопределенные местоимения some/any'", callback_data="start_test8")
keyboard.add(start_test)