from pydantic import BaseModel
from sqlalchemy import Column, Integer, String, BLOB
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class File(Base):
    __tablename__ = 'files'
    id = Column(Integer, primary_key=True)
    filename = Column(String, nullable=False)
    filepath = Column(String, nullable=False)
    file = Column(BLOB, nullable=False)






