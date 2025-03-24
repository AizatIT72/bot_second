from aiogram import types
from aiogram.dispatcher import FSMContext
from config.loader import bot
from states.support import Support
from data import sticker_data as kd
from data import text_data as hd

commands = ['/weather', '/reset_commands', '/support', '/help', '/start']
ADMIN = [994115172]
user_id1 = []
users_url = []
name_users = []
users_name = []

async def support_users(message: types.Message, state: FSMContext):
    global user_id
    user_id = message.chat.id
    global len_id
    len_id = len(str(user_id))
    user_url = message.from_user.url
    users_url.append(user_url) # ссылки на пользователей
    user_id1.append(user_id) # айди пользователей
    name_user = message.from_user.first_name
    name_users.append(name_user) # имена пользователей
    user_name = message.from_user.username
    users_name.append(user_name) # алиасы пользователей
    await bot.send_message(chat_id=message.chat.id, text=hd.DESCRIPTION_PROBLEMS)
    await Support().stage_1.set()


async def send_message_to_admin(message: types.Message, state: FSMContext):
    global answer
    answer = message.text
    if answer not in commands and answer is not None:
        await bot.send_message(chat_id=message.chat.id, text=hd.WAIT_ANSWER)
        await bot.send_sticker(sticker=kd.WAIT_ANSWER_STICKER, chat_id=message.chat.id)
        await bot.send_message(chat_id=994115172, text=hd.QUESTION_USER.format(answer, message.from_user.id, message.from_user.url,
                                                                               message.from_user.username))
    elif answer is None:
        await bot.send_message(chat_id=message.chat.id, text=hd.WARNING_IF_NOT_TEXT)
        user_id1.pop(0)
    else:
        await bot.send_message(chat_id=message.chat.id, text=hd.WARNING_IF_SEND_COMMANDS)
        user_id1.pop(0)
    await state.finish()

async def send_message_to_user(message: types.Message, state: FSMContext):
    answer1 = message.text
    try:
        if answer1[0:len_id] in str(user_id1):
            if len(user_id1) == 1:
                await bot.send_message(chat_id=user_id1[0],
                                       text=hd.CAME_ANSWER.format(name_users[0], answer1[len_id+1::], message.from_user.username))
                await bot.send_message(chat_id=994115172,
                                       text=hd.SUCCESS_SEND_MESSAGE_TO_USER.format(users_url[0], users_name[0]))
                user_id1.pop(0)
                users_url.pop(0)
                name_users.pop(0)
                users_name.pop(0)
            elif len(user_id1) > 1:
                await bot.send_message(chat_id=user_id1[0],
                                       text=hd.CAME_ANSWER.format(name_users[0], answer1[len_id+1::], message.from_user.username))
                await bot.send_message(chat_id=994115172,
                                       text=hd.SUCCESS_SEND_MESSAGE_TO_USER.format(users_url[0], users_name[0]))
                user_id1.pop(0)
                users_url.pop(0)
                name_users.pop(0)
                users_name.pop(0)
        else:
            await bot.send_message(chat_id=994115172, text=hd.NONE_COMMANDS)
    except:
        await bot.send_message(chat_id=994115172, text=hd.NONE_COMMANDS)
    await state.finish()