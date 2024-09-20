from sqlalchemy import Column, Integer, String
from database import Base
from pydantic import BaseModel, EmailStr

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(50), unique=True, index=True)
    email = Column(String(100), unique=True, index=True)
    password = Column(String(100))
    date_of_birth = Column(String(10)) # Format YYYY-MM-DD
    gender = Column(String(10))
    city = Column(String(50))
    state = Column(String(50))
    country = Column(String(50))

class UserCreate(BaseModel):
    username: str
    email: EmailStr
    password: str
    date_of_birth: str
    gender: str
    city: str
    state: str
    country: str
    
