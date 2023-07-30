from aiogram import types
from config.loader import bot
from keyboards.inline.tests_A1 import keyboard
from aiogram.dispatcher import FSMContext
from states.tests_A1 import Test_A1
from data.text_data import t1
import random

questions = [
    {
        'question': 'I ___ a student.',
        'answer': 'am'
    },
    {
        'question': 'She ___ a teacher.',
        'answer': 'is'
    },
    {
        'question': 'They ___ at home.',
        'answer': 'are'
    },
    {
        'question': 'He ___ my friend.',
        'answer': 'is'
    },
    {
        'question': 'We ___ in the park.',
        'answer': 'are'
    }
]
# res1 = ""
# global res1

async def start_test_a1_1(call: types.CallbackQuery):
    await bot.send_message(chat_id=call.message.chat.id, text=t1, reply_markup=keyboard)
    await call.answer()

async def questions_to_user_1(call: types.CallbackQuery, state: FSMContext):
    #global answer
    random_qa = random.choice(questions)
    question = random_qa['question']
    answer = random_qa['answer']
    await state.update_data(question=question, answer=answer)
    await bot.send_message(chat_id=call.from_user.id, text=f"Заполни пропуск в предложении(если хотите выйти из теста напишите /exit):"
                                                           f"\n\n{question}\n\nВарианты ответов:\n1) is, 2) are, 3) am")
    await Test_A1.stage_1.set()
    #await Test_A1.stage_1.set()


async def next_message_1(message: types.Message, state: FSMContext):
    user_answer = message.text
    #print(user_answer)
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
                                                           f"\n\n{question}\n\nВарианты ответов:\n1) is, 2) are, 3) am")
    #await state.finish()


