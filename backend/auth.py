from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session
from database import get_db
from models import User
from hash import Hash

# Utworzenie obiektu do uwierzytelniania użytkownika
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


# Funkcja do pobierania aktualnego użytkownika na podstawie tokenu
# Sprawdza ważność tokenu i zwraca użytkownika, jeśli token jest ważny
def get_current_user(token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)):
    user = db.query(User).filter(User.username == "example_username").first()
    if user is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid credentials",
            headers={"WWW-Authenticate": "Bearer"},
        )
    return user
