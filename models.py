from sqlalchemy import Column, Integer, String, ForeignKey
from database import Base
from pydantic import BaseModel, EmailStr
from sqlalchemy.orm import relationship

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

    goals = relationship("Goal", back_populates="user")

class UserCreate(BaseModel):
    username: str
    email: EmailStr
    password: str
    date_of_birth: str
    gender: str
    city: str
    state: str
    country: str

class Goal(Base):
    __tablename__ = "goals"

    id = Column(Integer, primary_key=True, index=True)
    goal_name = Column(String(100), index=True)
    description = Column(String(250), nullable=True)
    user_id=Column(Integer, ForeignKey("users.id"))

    #Relationship
    user=relationship("User", back_populates="goals")

class GoalCreate(BaseModel):
    goal_name: str
    description: str