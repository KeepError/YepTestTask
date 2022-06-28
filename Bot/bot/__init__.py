import os

from aiogram import Bot, Dispatcher
from aiogram.utils import executor


async def on_startup(dispatcher: Dispatcher):
    bot_info = await bot.get_me()
    print(f"Logged in as {bot_info.full_name} ({bot_info.mention})")


def start():
    executor.start_polling(dp, on_startup=on_startup, skip_updates=True)


bot = Bot(token=os.getenv("TELEGRAM_BOT_TOKEN"))
dp = Dispatcher(bot)
