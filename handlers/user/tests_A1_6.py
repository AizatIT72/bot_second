from aiogram import types
from config.loader import bot
from keyboards.inline.tests_A1_6 import keyboard
from aiogram.dispatcher import FSMContext
from states.tests_A1 import Test_A1
from data.text_data import t6
import random

questions = [
    {
        'question': 'My sister _______ speak three languages fluently.',
        'answer': 'can'
    },
    {
        'question': '_______ you please pass me the salt?',
        'answer': 'can'
    },
    {
        'question': 'They _______ solve the math problem quickly.',
        'answer': 'can'
    },
    {
        'question': 'I am sorry, I _______ attend the party tonight.',
        'answer': 'can not'
    },
    {
        'question': 'The baby _______ walk yet, but he is trying.',
        'answer': 'can not'
    },
    {
        'question': '_______ he swim across the river?',
        'answer': 'can'
    },
        {
        'question': 'We _______ see the stars clearly on a clear night.',
        'answer': 'can'
    },
    {
        'question': 'She _______ play the piano beautifully.',
        'answer': 'can'
    }
]

async def start_test_a1_6(call: types.CallbackQuery):
    await bot.send_message(chat_id=call.message.chat.id, text=t6, reply_markup=keyboard)
    await call.answer()

async def questions_to_user_6(call: types.CallbackQuery, state: FSMContext):
    #global answer
    random_qa = random.choice(questions)
    question = random_qa['question']
    answer = random_qa['answer']
    await state.update_data(question=question, answer=answer)
    await bot.send_message(chat_id=call.from_user.id, text=f"Заполни пропуск в предложении(если хотите выйти из теста напишите /exit):"
                                                           f"\n\n{question}\n\nВарианты ответов:\n1) can, 2) can not")
    await Test_A1.stage_6.set()


async def next_message_6(message: types.Message, state: FSMContext):
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
                                                           f"\n\n{question}\n\nВарианты ответов:\n1) can, 2) can not")