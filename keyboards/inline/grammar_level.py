from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

keyboard = InlineKeyboardMarkup(row_width=1)
a1_lvl = InlineKeyboardButton(text="A1", callback_data="a1")
a2_lvl = InlineKeyboardButton(text="A2", callback_data="a2")
b1_lvl = InlineKeyboardButton(text="B1", callback_data="b1")
b2_lvl = InlineKeyboardButton(text="B2", callback_data="b2")
keyboard.add(a1_lvl, a2_lvl, b1_lvl, b2_lvl)