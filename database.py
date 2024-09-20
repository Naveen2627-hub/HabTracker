from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from urllib.parse import quote

username = "root"
password = "Njoyllu@143"
DATABASE_URL = f"mysql+mysqlconnector://{username}:{quote(password)}@localhost/habit_tracker"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit = False, autoflush = False, bind=engine)
Base = declarative_base()