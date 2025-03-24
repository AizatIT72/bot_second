from aiogram import types
from config.loader import bot
from keyboards.inline.tests_A1_7 import keyboard
from aiogram.dispatcher import FSMContext
from states.tests_A1 import Test_A1
from data.text_data import t7
import random

questions = [
    {
        'question': '_______ am going to the park.',
        'answer': 'I'
    },
    {
        'question': '_______ like to play football.',
        'answer': 'We'
    },
    {
        'question': '_______ is a doctor.',
        'answer': 'He'
    },
    {
        'question': '_______ have a pet cat.',
        'answer': 'We'
    },
    {
        'question': '_______ are going to the movies.',
        'answer': 'They'
    },
    {
        'question': '_______ is my sister.',
        'answer': 'She'
    },
        {
        'question': '_______ is a nice day.',
        'answer': 'It'
    },
    {
        'question': '_______ are studying for the test.',
        'answer': 'They'
    }
]

async def start_test_a1_7(call: types.CallbackQuery):
    await bot.send_message(chat_id=call.message.chat.id, text=t7, reply_markup=keyboard)
    await call.answer()

async def questions_to_user_7(call: types.CallbackQuery, state: FSMContext):
    #global answer
    random_qa = random.choice(questions)
    question = random_qa['question']
    answer = random_qa['answer']
    await state.update_data(question=question, answer=answer)
    await bot.send_message(chat_id=call.from_user.id, text=f"Заполни пропуск в предложении(если хотите выйти из теста напишите /exit):"
                                                           f"\n\n{question}\n\nВарианты ответов:\n1) I, 2) we, 3) you, 4) they, 5) he, 6) she, 7) it")
    await Test_A1.stage_7.set()


async def next_message_7(message: types.Message, state: FSMContext):
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
                                                           f"\n\n{question}\n\nВарианты ответов:\n1) I, 2) we, 3) you, 4) they, 5) he, 6) she, 7) it")