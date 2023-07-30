from aiogram import types
from config.loader import bot
from keyboards.inline.tests_A1_3 import keyboard
from aiogram.dispatcher import FSMContext
from states.tests_A1 import Test_A1
from data.text_data import t3
import random

questions = [
    {
        'question': '_______ a cat on the roof.',
        'answer': 'There is'
    },
    {
        'question': '_______ some books on the shelf.',
        'answer': 'There are'
    },
    {
        'question': '_______ a lot of people at the party.',
        'answer': 'There are'
    },
    {
        'question': '_______ some milk in the fridge.',
        'answer': 'There is'
    },
    {
        'question': '_______ two apples on the table.',
        'answer': 'There are'
    }
]

async def start_test_a1_3(call: types.CallbackQuery):
    await bot.send_message(chat_id=call.message.chat.id, text=t3, reply_markup=keyboard)
    await call.answer()

async def questions_to_user_3(call: types.CallbackQuery, state: FSMContext):
    #global answer
    random_qa = random.choice(questions)
    question = random_qa['question']
    answer = random_qa['answer']
    await state.update_data(question=question, answer=answer)
    await bot.send_message(chat_id=call.from_user.id, text=f"Заполни пропуск в предложении(если хотите выйти из теста напишите /exit):"
                                                           f"\n\n{question}\n\nВарианты ответов:\n1) There is, 2) There are")
    await Test_A1.stage_3.set()


async def next_message_3(message: types.Message, state: FSMContext):
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
                                                           f"\n\n{question}\n\nВарианты ответов:\n1) There is, 2) There are")