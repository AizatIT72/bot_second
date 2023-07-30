from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

keyboard = InlineKeyboardMarkup()
start_test = InlineKeyboardButton(text="Пройти тест на тему 'Притяжательные местоимения my/our/your/his/her/its'", callback_data="start_test10")
keyboard.add(start_test)