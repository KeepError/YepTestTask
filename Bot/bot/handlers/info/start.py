from aiogram import types


async def start_command(msg: types.Message):
    """Send start message"""

    text = "Start message..."

    await msg.answer(text)
