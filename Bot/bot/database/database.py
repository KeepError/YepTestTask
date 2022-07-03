import sqlalchemy
from sqlalchemy import orm

from .models import Base


class Database:
    def __init__(self, obj):
        engine = sqlalchemy.create_engine(obj, echo=False)
        session_factory = orm.sessionmaker(bind=engine)
        self._session: orm.Session = session_factory()

        Base.metadata.create_all(engine)

    def get_session(self) -> orm.Session:
        return self._session
