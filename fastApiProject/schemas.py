from pydantic import BaseModel

class UserCreate(BaseModel):
    username: str
    email: str
    password: str

class User(BaseModel):
    username: str
    email: str
    role: str

class ItemCreate(BaseModel):
    title: str
    description: str

class Item(BaseModel):
    id: int
    title: str
    description: str
