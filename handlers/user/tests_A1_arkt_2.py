from aiogram import types
from config.loader import bot
from keyboards.inline.tests_A1_2 import keyboard
from aiogram.dispatcher import FSMContext
from states.tests_A1 import Test_A1
from data.text_data import t2
import random

questions = [
    {
        'question': 'Can I have _______ apple from the fruit basket?',
        'answer': 'a'
    },
    {
        'question': 'My sister wants to be _______ astronaut when she grows up.',
        'answer': 'an'
    },
    {
        'question': 'I saw _______ shooting star in the sky last night.',
        'answer': 'a'
    },
    {
        'question': 'There is _______ interesting book on the shelf.',
        'answer': 'an'
    },
    {
        'question': '_______ elephant is the largest land animal.',
        'answer': 'the'
    },
        {
        'question': 'My friend has _______ black cat named Luna.',
        'answer': 'a'
    },
    {
        'question': '_______ sun rises in the east and sets in the west.',
        'answer': 'the'
    },
    {
        'question': 'I need to buy _______ new laptop for school.',
        'answer': 'a'
    },
    {
        'question': 'She saw _______ rainbow after the rain.',
        'answer': 'a'
    },
    {
        'question': '_______ Eiffel Tower is located in Paris.',
        'answer': 'the'
    }
]

async def start_test_a1_2(call: types.CallbackQuery):
    await bot.send_message(chat_id=call.message.chat.id, text=t2, reply_markup=keyboard)
    await call.answer()

async def questions_to_user_2(call: types.CallbackQuery, state: FSMContext):
    #global answer
    random_qa = random.choice(questions)
    question = random_qa['question']
    answer = random_qa['answer']
    await state.update_data(question=question, answer=answer)
    await bot.send_message(chat_id=call.from_user.id, text=f"Заполни пропуск в предложении(если хотите выйти из теста напишите /exit):"
                                                           f"\n\n{question}\n\nВарианты ответов:\n1) a, 2) an, 3) the")
    await Test_A1.stage_2.set()
    #await Test_A1.stage_1.set()


async def next_message_2(message: types.Message, state: FSMContext):
    user_answer = message.text
    #print(user_answer)
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
                                                           f"\n\n{question}\n\nВарианты ответов:\n1) a, 2) an, 3) the")