from pydantic import BaseModel, Field, field_validator
from typing import Optional
from datetime import datetime

class UserBase(BaseModel):
    username: str
    email: str
    password: str

class UserDisplay(BaseModel):
    username: str
    email: str

    class Config():
        orm_mode = True

class RideBase(BaseModel):
    departure: str
    destination: str
    date: str
    time: str
    passengers: int
    phone_number: str

class RideDisplay(RideBase):
    class Config():
        orm_mode = True

class RideSearch(BaseModel):
    departure: str
    destination: str
    date: str

    @field_validator('date')
    def format_date(cls, value):
        try:
            return datetime.strptime(value, '%Y-%m-%d').strftime('%d.%m.%Y')
        except ValueError:
            raise ValueError("Incorrect date format, should be YYYY-MM-DD")

class Login(BaseModel):
    username: str
    password: str
