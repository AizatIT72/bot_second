from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

keyboard = InlineKeyboardMarkup(row_width=1)
book1 = InlineKeyboardButton(text="Памела Линдон Трэверс: повесть 'Мэри Поппинс'", callback_data="book1", url="https://anylang.net/ru/books/en/meri-poppins/read")
book2 = InlineKeyboardButton(text="Антуан де Сент-Экзюпери: повесть 'Маленький принц'", callback_data="book2", url="https://anylang.net/ru/books/en/malenkiy-princ/read")
book3 = InlineKeyboardButton(text="Анна Тодд: роман 'После'", callback_data="book3", url="https://anylang.net/ru/books/en/posle/read")
book4 = InlineKeyboardButton(text="Говард Пайл: 'История сэра Ланселота и его спутников'", url="https://anylang.net/ru/books/en/istoriya-sera-lanselota-i-ego-sputnikov")
keyboard.add(book1, book2, book3, book4)