from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

keyboard = InlineKeyboardMarkup()
start_test = InlineKeyboardButton(text="Пройти тест на тему 'Указательные местоимения this/that/these/those'", callback_data="start_test9")
keyboard.add(start_test)