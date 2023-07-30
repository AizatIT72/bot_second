from aiogram import types
from config.loader import bot
from keyboards.inline.tests_A1_11 import keyboard
from aiogram.dispatcher import FSMContext
from states.tests_A1 import Test_A1
from data.text_data import t11
import random

questions = [
    {
        'question': 'She _______ arrives on time for class.',
        'answer': 'always'
    },
    {
        'question': 'They _______ go to the beach in the summer.',
        'answer': 'often'
    },
    {
        'question': 'He _______ forgets to call his parents.',
        'answer': 'never'
    },
    {
        'question': 'We _______ take the bus to work.',
        'answer': 'never'
    },
    {
        'question': 'I _______ drink coffee in the evening.',
        'answer': 'never'
    }
]

async def start_test_a1_11(call: types.CallbackQuery):
    await bot.send_message(chat_id=call.message.chat.id, text=t11, reply_markup=keyboard)
    await call.answer()

async def questions_to_user_11(call: types.CallbackQuery, state: FSMContext):
    #global answer
    random_qa = random.choice(questions)
    question = random_qa['question']
    answer = random_qa['answer']
    await state.update_data(question=question, answer=answer)
    await bot.send_message(chat_id=call.from_user.id, text=f"Заполни пропуск в предложении(если хотите выйти из теста напишите /exit):"
                                                           f"\n\n{question}\n\nВарианты ответов:\n1) always, 2) often, 3) never")
    await Test_A1.stage_11.set()


async def next_message_11(message: types.Message, state: FSMContext):
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
                                                           f"\n\n{question}\n\nВарианты ответов:\n1) always, 2) often, 3) never")