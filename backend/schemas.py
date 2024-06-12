from pydantic import BaseModel

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
    user_id: int

class RideDisplay(RideBase):
    class Config():
        orm_mode = True

class RideSearch(BaseModel):
    departure: str
    destination: str
    date: str

class Login(BaseModel):
    username: str
    password: str
