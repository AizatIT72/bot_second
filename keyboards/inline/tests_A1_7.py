from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

keyboard = InlineKeyboardMarkup()
start_test = InlineKeyboardButton(text="Пройти тест на тему 'Личные местоимения I, we, you, they, he, she, it'", callback_data="start_test7")
keyboard.add(start_test)