from sqlalchemy import Column, Integer, String
from database import Base

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    email = Column(String, unique=True, index=True)
    password = Column(String)

class Ride(Base):
    __tablename__ = "rides"
    id = Column(Integer, primary_key=True, index=True)
    departure = Column(String, index=True)
    destination = Column(String, index=True)
    date = Column(String)
    time = Column(String)
    passengers = Column(Integer)
    phone_number = Column(String)
    user_id = Column(Integer)
