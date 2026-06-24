from sqlalchemy import engine
from sqlalchemy.orm import DeclarativeBase
from dotenv import load_dotenv
import os

load_dotenv()

DB_source = engine.create_engine(os.getenv("DB_URL"),echo=True)

class Base(DeclarativeBase):
    pass
