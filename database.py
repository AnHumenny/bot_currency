from sqlalchemy import Column, Integer, String, Date, BOOLEAN, DateTime
from datetime import datetime
from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine
from sqlalchemy.orm import DeclarativeBase
import os
from dotenv import load_dotenv

load_dotenv()

engine = create_async_engine(
    f"mysql+asyncmy://{os.getenv('user')}:{os.getenv('password')}@{os.getenv('host')}/{os.getenv('database')}"
)

new_session = async_sessionmaker(engine, expire_on_commit=False)

class Model(DeclarativeBase):
    id = Column(Integer, primary_key=True, autoincrement=True)

class DCurrent(Model):
    __tablename__ = "current"
    actual_current = Column(String(15))
    date = Column(DateTime, default=datetime.utcnow)
    type_current = Column(String(5))

class DUser(Model):
    __tablename__ = "users"
    login = Column(String(30))
    name = Column(String(30))
    status = Column(String(15))
    password = Column(BOOLEAN)
    phone = Column(String(14))
    email = Column(String(50))
    tg_id = Column(String(50))

class DStat(Model):
    __tablename__ = "stat_current"
    actual_current = Column(String(15))
    date = Column(Date, default=datetime.utcnow)
    type_current = Column(String(5))
