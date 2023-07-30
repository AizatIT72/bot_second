from aiogram import Dispatcher
import logging
from aiogram.utils import executor
from config.loader import dp, bot
import handlers
from config.config import WEBHOOK_URL

async def on_startup(dispatcher: Dispatcher):
    await bot.set_webhook((WEBHOOK_URL))
    handlers.setup(dispatcher)

async def on_shutdown(dispatcher: Dispatcher):
    logging.warning('Отключаем')
    await bot.delete_webhook()
    await dispatcher.storage.close()
    await dispatcher.storage.wait_closed()
    logging.warning('Пока')


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup, on_shutdown=on_shutdown)