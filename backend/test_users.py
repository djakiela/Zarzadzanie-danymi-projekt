from app import app, db
from models import User

# Utworzenie kontekstu aplikacji
with app.app_context():
    # Pobranie wszystkich użytkowników
    users = User.query.all()

    # Wyświetlenie użytkowników
    for user in users:
        print(f"Username: {user.username}, Email: {user.email}, Password Hash: {user.password_hash}")
