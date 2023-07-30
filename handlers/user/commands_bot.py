from aiogram import Bot, types
from aiogram.types import BotCommand, BotCommandScopeChat


async def set_starting_commands(bot: Bot, chat_id: int):
    COMMANDS = {
        'ru': [
            BotCommand("start", "Начать использовать бота"),
            BotCommand("support", "Техподдержка")
        ]
    }
    for language_code, commands in COMMANDS.items():
        await bot.set_my_commands(
            commands=commands,
            scope=BotCommandScopeChat(chat_id),
            language_code=language_code
        )

async def message_reset_commands(message: types.Message):
    await message.bot.delete_my_commands(BotCommandScopeChat(message.from_user.id))
    await message.bot.delete_my_commands(BotCommandScopeChat(message.from_user.id), language_code='ru')
    await message.reply('Все команды удалены')
