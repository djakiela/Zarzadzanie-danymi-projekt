from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URL = "sqlite:///./fastapi-database.db"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


# Ustawienie bazowej klasy deklaratywnej
Base = declarative_base()

# Funkcja do pobierania sesji bazy danych
# Zapewnia zarządzanie sesją bazy danych
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
