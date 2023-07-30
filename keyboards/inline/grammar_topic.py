from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

keyboard = InlineKeyboardMarkup()
to_be = InlineKeyboardButton(text="1)Глагол to be", callback_data="to_be")
arkt = InlineKeyboardButton(text="2)Артикли a/an, the", callback_data="arkt")
there = InlineKeyboardButton(text="3)There is/are", callback_data="there")
question = InlineKeyboardButton(text="4)Вопросы с what, who, where, why, why", callback_data="question")
first_second_nums = InlineKeyboardButton(text="5)Единственное и множественное число существительных (-s, -es)", callback_data="nums")
modal_verb = InlineKeyboardButton(text="6)Модальный глагол can/can't", callback_data="modal")
pron = InlineKeyboardButton(text="7)Личные местоимения I, we, you, they, he, she, it", callback_data="pron")
noun_pron = InlineKeyboardButton(text="8)Неопределенные местоимения some/any", callback_data="noun_pron")
ukaz_pron = InlineKeyboardButton(text="9)Указательные местоимения this/that/these/those", callback_data="ukaz_pron")
prit_pron = InlineKeyboardButton(text="10)Притяжательные местоимения my, our, your, his, her, its", callback_data="prit_pron")
nar = InlineKeyboardButton(text="11)Наречия частотности always, often, never", callback_data="nar")
present_simple = InlineKeyboardButton(text="12)Present Simple", callback_data="pr_s")
past_simple = InlineKeyboardButton(text="13)Past Simple", callback_data="ps_s")
future_simple = InlineKeyboardButton(text="14)Future Simple", callback_data="fut_s")
present_cont = InlineKeyboardButton(text="15)Present Continuous (для описания действий, которые происходят сейчас)",
                                    callback_data="pr_c")
keyboard.add(to_be, arkt, there, question, first_second_nums, modal_verb, pron, noun_pron, ukaz_pron, prit_pron,
             nar, present_simple, past_simple, future_simple, present_cont)