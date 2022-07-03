from aiogram import Dispatcher

from .logs import LogsMiddleware


def setup(dp: Dispatcher):
    dp.middleware.setup(LogsMiddleware())
