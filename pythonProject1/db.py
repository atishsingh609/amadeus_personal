from sqlalchemy import create_engine
from sqlalchemy.orm import Session

from schema import Base

engine = create_engine('sqlite:///database.db')
Base.metadata.create_all(engine)

def get_session():
    session = Session(bind=engine)
    yield session