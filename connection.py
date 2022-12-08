from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session

from .models import *
from .models import Base

__all__ = []
 
class DBConnection:

    def __init__(self):
        self._engine = create_engine(f"sqlite:///file/whatever")

        self._session_factory = sessionmaker(bind=self._engine)
        self._session = scoped_session(self._session_factory)

    @property
    def engine(self):
        return self._engine

    @property
    def session(self):
        return self._session
 
    def create_all_tables(self):
        Base.metadata.create_all(self.engine)
                                      
    def drop_all_tables(self):
        Base.metadata.drop_all(self.engine)

__all__ += ['DBConnection']
