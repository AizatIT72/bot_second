from aiogram import types
from config.loader import bot
from keyboards.inline.tests_A1_9 import keyboard
from aiogram.dispatcher import FSMContext
from states.tests_A1 import Test_A1
from data.text_data import t9
import random

questions = [
    {
        'question': '_______ is my favorite book.',
        'answer': 'This'
    },
    {
        'question': '_______ are my keys. Thank you for finding them!',
        'answer': 'These'
    },
    {
        'question': 'I like _______ song on the radio.',
        'answer': 'That'
    },
    {
        'question': '_______ flowers in the garden are beautiful.',
        'answer': 'These'
    },
    {
        'question': '_______ book on the shelf is very interesting.',
        'answer': 'This'
    }
]

async def start_test_a1_9(call: types.CallbackQuery):
    await bot.send_message(chat_id=call.message.chat.id, text=t9, reply_markup=keyboard)
    await call.answer()

async def questions_to_user_9(call: types.CallbackQuery, state: FSMContext):
    #global answer
    random_qa = random.choice(questions)
    question = random_qa['question']
    answer = random_qa['answer']
    await state.update_data(question=question, answer=answer)
    await bot.send_message(chat_id=call.from_user.id, text=f"Заполни пропуск в предложении(если хотите выйти из теста напишите /exit):"
                                                           f"\n\n{question}\n\nВарианты ответов:\n1) This, 2) That, 3) These, 4) Those")
    await Test_A1.stage_9.set()


async def next_message_9(message: types.Message, state: FSMContext):
    user_answer = message.text
    if user_answer == '/exit':
        await state.finish()
        await message.answer("Тест завершен")
    else:
        async with state.proxy() as data:
            question = data['question']
            answer = data['answer']

        if user_answer == answer:
            await bot.send_message(chat_id=message.chat.id, text="Верно✅")
        else:
            await bot.send_message(chat_id=message.chat.id, text="Неверно❌")
            await message.answer(f"Правильный ответ: {answer}")
        random_qa = random.choice(questions)
        question = random_qa['question']
        answer = random_qa['answer']
        await state.update_data(question=question, answer=answer)
        await message.answer(f"Заполни пропуск в предложении(если хотите выйти из теста напишите /exit):"
                                                           f"\n\n{question}\n\nВарианты ответов:\n1) This, 2) That, 3) These, 4) Those")