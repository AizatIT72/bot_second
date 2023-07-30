from aiogram import types
from config.loader import bot
from keyboards.inline.tests_A1_10 import keyboard
from aiogram.dispatcher import FSMContext
from states.tests_A1 import Test_A1
from data.text_data import t10
import random

questions = [
    {
        'question': 'This is _______ book.',
        'answer': 'my'
    },
    {
        'question': 'They are visiting _______ grandparents.',
        'answer': 'our'
    },
    {
        'question': 'His car is parked over there. _______ car is the red one.',
        'answer': 'her'
    },
    {
        'question': 'She invited us to _______ birthday party.',
        'answer': 'our'
    },
    {
        'question': 'The cat is washing _______ paws.',
        'answer': 'its'
    }
]

async def start_test_a1_10(call: types.CallbackQuery):
    await bot.send_message(chat_id=call.message.chat.id, text=t10, reply_markup=keyboard)
    await call.answer()

async def questions_to_user_10(call: types.CallbackQuery, state: FSMContext):
    #global answer
    random_qa = random.choice(questions)
    question = random_qa['question']
    answer = random_qa['answer']
    await state.update_data(question=question, answer=answer)
    await bot.send_message(chat_id=call.from_user.id, text=f"Заполни пропуск в предложении(если хотите выйти из теста напишите /exit):"
                                                           f"\n\n{question}\n\nВарианты ответов:\n1) my, 2) our, 3) your, 4) his, 5) her, 6) its")
    await Test_A1.stage_10.set()


async def next_message_10(message: types.Message, state: FSMContext):
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
                                                           f"\n\n{question}\n\nВарианты ответов:\n1) my, 2) our, 3) your, 4) his, 5) her, 6) its")