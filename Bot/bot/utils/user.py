from bot.database import User
from bot import database


def get_user_by_telegram_id(telegram_id: int) -> User:
    session = database.get_session()
    user = session.query(User).filter(User.telegram_id == telegram_id).scalar()
    if user is None:
        user = User(telegram_id=telegram_id)
        session.add(user)
        session.commit()
    return user
