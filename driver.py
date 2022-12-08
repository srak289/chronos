from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session

from .models import *
from .models import Base

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

class Chronos:

    prompt = 'chronos> '
    cmd_list = frozenset({'help', 'create', 'get', 'set', 'delete'})
    ap = argparse.ArgumentParser()
    ap

    def __init__(self):
        connection = DBConnection()
        connection.create_all_tables()
        self.session = connection.session

    def interact(self):
        while True:
            i = input(self.prompt)
            print(f'You said: {i}')

if __name__ == '__main__':
    ap = argparse.ArgumentParser()
    ap.add_argument()
    
    eg = ap.add_mutually_exclusive_group()

    chronos = Chronos()

    if ap.interact: chronos.interact()
