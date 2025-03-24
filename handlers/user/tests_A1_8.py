from aiogram import types
from config.loader import bot
from keyboards.inline.tests_A1_8 import keyboard
from aiogram.dispatcher import FSMContext
from states.tests_A1 import Test_A1
from data.text_data import t8
import random

questions = [
    {
        'question': 'Is there _______ milk in the fridge?',
        'answer': 'any'
    },
    {
        'question': 'I have _______ good news to share with you.',
        'answer': 'some'
    },
    {
        'question': 'She asked if there were _______ cookies left.',
        'answer': 'any'
    },
    {
        'question': 'We did not find _______ information about the event.',
        'answer': 'any'
    },
    {
        'question': 'Can you lend me _______ money until payday?',
        'answer': 'some'
    },
    {
        'question': 'There are not _______ apples in the basket.',
        'answer': 'any'
    },
        {
        'question': 'He brought _______ snacks for the party.',
        'answer': 'some'
    },
    {
        'question': 'Do you have _______ plans for the weekend?',
        'answer': 'some'
    }
]

async def start_test_a1_8(call: types.CallbackQuery):
    await bot.send_message(chat_id=call.message.chat.id, text=t8, reply_markup=keyboard)
    await call.answer()

async def questions_to_user_8(call: types.CallbackQuery, state: FSMContext):
    #global answer
    random_qa = random.choice(questions)
    question = random_qa['question']
    answer = random_qa['answer']
    await state.update_data(question=question, answer=answer)
    await bot.send_message(chat_id=call.from_user.id, text=f"Заполни пропуск в предложении(если хотите выйти из теста напишите /exit):"
                                                           f"\n\n{question}\n\nВарианты ответов:\n1) some, 2) any")
    await Test_A1.stage_8.set()


async def next_message_8(message: types.Message, state: FSMContext):
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
                                                           f"\n\n{question}\n\nВарианты ответов:\n1) some, 2) any")