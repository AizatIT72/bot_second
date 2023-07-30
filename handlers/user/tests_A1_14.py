from aiogram import types
from config.loader import bot
from keyboards.inline.tests_A1_14 import keyboard
from aiogram.dispatcher import FSMContext
from states.tests_A1 import Test_A1
from data.text_data import t14
import random

questions = [
    {
        'question': 'I _______ (will/will not) go to the beach tomorrow.',
        'answer': 'will'
    },
    {
        'question': 'She _______ (will/will not) visit her grandparents next weekend.',
        'answer': 'will'
    },
    {
        'question': 'They _______ (will/will not) study for the exam tonight.',
        'answer': 'will not'
    },
    {
        'question': '_______ (Will/Will not) you join us for dinner?',
        'answer': 'Will'
    },
    {
        'question': 'He _______ (will/will not) travel to Europe next summer.',
        'answer': 'will'
    }
]

async def start_test_a1_14(call: types.CallbackQuery):
    await bot.send_message(chat_id=call.message.chat.id, text=t14, reply_markup=keyboard)
    await call.answer()

async def questions_to_user_14(call: types.CallbackQuery, state: FSMContext):
    random_qa = random.choice(questions)
    question = random_qa['question']
    answer = random_qa['answer']
    await state.update_data(question=question, answer=answer)
    await bot.send_message(chat_id=call.from_user.id, text=f"Заполни пропуск в предложении(если хотите выйти из теста напишите /exit):"
                                                           f"\n\n{question}")
    await call.answer()
    await Test_A1.stage_14.set()


async def next_message_14(message: types.Message, state: FSMContext):
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