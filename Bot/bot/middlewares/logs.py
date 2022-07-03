from datetime import datetime

from aiogram import types
from aiogram.dispatcher.handler import current_handler
from aiogram.dispatcher.middlewares import BaseMiddleware

from bot.utils.user import get_user_by_telegram_id
from bot import database


class LogsMiddleware(BaseMiddleware):
    """Middleware to write Prometheus metrics on user's actions"""

    def __init__(self):
        super(LogsMiddleware, self).__init__()

    # noinspection PyMethodMayBeStatic
    async def on_process_message(self, message: types.Message, data: dict):
        """Write Message logs"""

        handler = current_handler.get()
        handler_name = handler.__name__ if handler else "-"

        command = message.get_command()
        command_name = command if command else "-"

        user = get_user_by_telegram_id(message.from_user.id)
        if not user.first_message:
            user.first_message = datetime.now()
        user.last_message = datetime.now()
        database.get_session().commit()

    # noinspection PyMethodMayBeStatic
    async def on_process_callback_query(self, callback_query: types.CallbackQuery, data: dict):
        """Write Callback query logs"""

        handler = current_handler.get()
        handler_name = handler.__name__ if handler else "-"

        callback_query_data = callback_query.data
        callback_query_data_name = callback_query_data if callback_query else "-"
