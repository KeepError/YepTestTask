from sqlalchemy import Column, Integer, String, DateTime

from ._base import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    telegram_id = Column(Integer, index=True, nullable=False)
    name = Column(String, nullable=True)
    surname = Column(String, nullable=True)
    organization = Column(String, nullable=True)
    first_message = Column(DateTime, nullable=True)
    last_message = Column(DateTime, nullable=True)
