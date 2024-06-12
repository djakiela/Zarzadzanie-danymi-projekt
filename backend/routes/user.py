from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from schemas import UserBase, UserDisplay, Login
from models import User
from database import get_db
from hash import Hash

router = APIRouter(prefix="/user", tags=["user"])

@router.post("/", response_model=UserDisplay)
def create_user(request: UserBase, db: Session = Depends(get_db)):
    new_user = User(
        username=request.username,
        email=request.email,
        password=Hash.bcrypt(request.password)
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

@router.post("/login")
def login(request: Login, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.username == request.username).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    if not Hash.verify(user.password, request.password):
        raise HTTPException(status_code=401, detail="Incorrect password")
    return {"message": "Login successful"}

@router.get("/{id}", response_model=UserDisplay)
def get_user(id: int, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.id == id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user
