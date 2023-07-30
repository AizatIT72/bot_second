from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

keyboard = InlineKeyboardMarkup()
reading = InlineKeyboardButton(text="Чтение", callback_data="read")
grammar_lang = InlineKeyboardButton(text="Грамматика", callback_data="grammar")
vocabulary = InlineKeyboardButton(text="Лексика", callback_data="vocab")
level_lang = InlineKeyboardButton(text="Уровни языка", callback_data="lang")
keyboard.add(reading, grammar_lang, vocabulary, level_lang)