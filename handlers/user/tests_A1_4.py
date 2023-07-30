from aiogram import types
from config.loader import bot
from keyboards.inline.tests_A1_4 import keyboard
from aiogram.dispatcher import FSMContext
from states.tests_A1 import Test_A1
from data.text_data import t4
import random

questions = [
    {
        'question': '_______ is your name?',
        'answer': 'Who'
    },
    {
        'question': '_______ did you go last weekend?',
        'answer': 'Where'
    },
    {
        'question': '_______ many books are on the shelf?',
        'answer': 'How Much'
    },
    {
        'question': '_______ is the capital of France?',
        'answer': 'What'
    },
    {
        'question': '_______ are you feeling today?',
        'answer': 'What'
    },
    {
        'question': '_______ do you usually go to school?',
        'answer': 'When'
    },
        {
        'question': '_______ does it cost to buy a ticket to the zoo?',
        'answer': 'How'
    },
    {
        'question': '_______ is your best friend?',
        'answer': 'Who'
    },
    {
        'question': '_______ are you studying for the exam?',
        'answer': 'What'
    },
    {
        'question': '_______ did you bake this delicious cake?',
        'answer': 'When'
    }
]

async def start_test_a1_4(call: types.CallbackQuery):
    await bot.send_message(chat_id=call.message.chat.id, text=t4, reply_markup=keyboard)
    await call.answer()

async def questions_to_user_4(call: types.CallbackQuery, state: FSMContext):
    #global answer
    random_qa = random.choice(questions)
    question = random_qa['question']
    answer = random_qa['answer']
    await state.update_data(question=question, answer=answer)
    await bot.send_message(chat_id=call.from_user.id, text=f"Заполни пропуск в предложении(если хотите выйти из теста напишите /exit):"
                                                           f"\n\n{question}\n\nВарианты ответов:\n1) What, 2) Who, 3) Where, 4) When, 5) Why, 6) How, 7) How much(many)")
    await Test_A1.stage_4.set()


async def next_message_4(message: types.Message, state: FSMContext):
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
                                                           f"\n\n{question}\n\nВарианты ответов:\n1) What, 2) Who, 3) Where, 4) When, 5) Why, 6) How, 7) How much(many)")