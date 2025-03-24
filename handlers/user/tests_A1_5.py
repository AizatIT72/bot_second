from aiogram import types
from config.loader import bot
from keyboards.inline.tests_A1_5 import keyboard
from aiogram.dispatcher import FSMContext
from states.tests_A1 import Test_A1
from data.text_data import t5
import random

questions = [
    {
        'question': 'My friend has two _______ (child/children).',
        'answer': 'children'
    },
    {
        'question': 'The old man feeds the _______ (bird/birds) every morning.',
        'answer': 'birds'
    },
    {
        'question': 'There are five _______ (box/boxes) in the room.',
        'answer': 'boxes'
    },
    {
        'question': 'The _______ (bus/buses) arrived at the station.',
        'answer': 'buses'
    },
    {
        'question': 'She bought three _______ (dress/dresses) for the party.',
        'answer': 'dresses'
    },
    {
        'question': 'The teacher praised the _______ (student/students) for their hard work.',
        'answer': 'students'
    },
        {
        'question': 'I need to buy some _______ (fruit/fruits) from the market.',
        'answer': 'fruit'
    },
    {
        'question': 'The _______ (leaf/leaves) fell from the tree in autumn.',
        'answer': 'leaves'
    },
    {
        'question': 'The _______ (knife/knives) in the kitchen are very sharp.',
        'answer': 'knives'
    },
    {
        'question': 'The _______ (child/children) are playing in the park.',
        'answer': 'children'
    }
]

async def start_test_a1_5(call: types.CallbackQuery):
    await bot.send_message(chat_id=call.message.chat.id, text=t5, reply_markup=keyboard)
    await call.answer()

async def questions_to_user_5(call: types.CallbackQuery, state: FSMContext):
    #global answer
    random_qa = random.choice(questions)
    question = random_qa['question']
    answer = random_qa['answer']
    await state.update_data(question=question, answer=answer)
    await bot.send_message(chat_id=call.from_user.id, text=f"Заполни пропуск в предложении(если хотите выйти из теста напишите /exit):"
                                                           f"\n\n{question}")
    await Test_A1.stage_5.set()


async def next_message_5(message: types.Message, state: FSMContext):
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