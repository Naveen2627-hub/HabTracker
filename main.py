from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from database import SessionLocal, engine, Base
from models import User, UserCreate
import hashlib


app = FastAPI()

Base.metadata.create_all(bind=engine)

# To get database session
def get_db():
    db = SessionLocal()
    try: 
        yield db
    finally:
        db.close()

# User Signup EndPoint
@app.post("/signup/")
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    hashed_password = hashlib.sha256(user.password.encode()).hexdigest()

    db_user = User(
        username=user.username, 
        email=user.email, 
        password = hashed_password,
        date_of_birth = user.date_of_birth,
        gender = user.gender,
        city=user.city,
        state=user.state,
        country=user.country
        )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)


    return db_user