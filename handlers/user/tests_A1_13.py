from aiogram import types
from config.loader import bot
from keyboards.inline.tests_A1_13 import keyboard
from aiogram.dispatcher import FSMContext
from states.tests_A1 import Test_A1
from data.text_data import t13
import random

questions = [
    {
        'question': 'She _______ (buy) a new car last month.',
        'answer': 'bought'
    },
    {
        'question': 'They _______ (go) to the park yesterday.',
        'answer': 'went'
    },
    {
        'question': 'We _______ (eat) pizza for dinner last night.',
        'answer': 'ate'
    },
    {
        'question': '_______ (Did/Did not) you _______ (see) the movie last weekend?',
        'answer': 'did, see'
    },
    {
        'question': 'He _______ (drink) coffee this morning.',
        'answer': 'drank'
    }
]

async def start_test_a1_13(call: types.CallbackQuery):
    await bot.send_message(chat_id=call.message.chat.id, text=t13, reply_markup=keyboard)
    await call.answer()

async def questions_to_user_13(call: types.CallbackQuery, state: FSMContext):
    #global answer
    random_qa = random.choice(questions)
    question = random_qa['question']
    answer = random_qa['answer']
    await state.update_data(question=question, answer=answer)
    await bot.send_message(chat_id=call.from_user.id, text=f"Заполни пропуск в предложении(если хотите выйти из теста напишите /exit):"
                                                           f"\n\n{question}")
    await Test_A1.stage_13.set()


async def next_message_13(message: types.Message, state: FSMContext):
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
                                                           f"\n\n{question}")