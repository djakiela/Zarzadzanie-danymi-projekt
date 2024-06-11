import requests

# URL do API Flask
BASE_URL = "http://127.0.0.1:5000/api"

# Dane logowania
login_data = {
    "username": "Przewoźnik",
    "password": "1234"
}

# Funkcja do logowania
def login():
    url = f"{BASE_URL}/login"
    session = requests.Session()  # Używamy sesji, aby zarządzać ciasteczkami
    response = session.post(url, json=login_data)
    if response.status_code == 200:
        print("Logged in successfully!")
        print("Response:", response.json())
        return session  # Zwracamy sesję
    else:
        print("Failed to log in.")
        print("Status code:", response.status_code)
        print("Response:", response.json())
        return None

# Funkcja do wylogowania
def logout(session):
    url = f"{BASE_URL}/logout"
    response = session.post(url)
    if response.status_code == 200:
        print("Logged out successfully!")
        print("Response:", response.json())
    else:
        print("Failed to log out.")
        print("Status code:", response.status_code)
        print("Response:", response.text)

# Testowanie logowania i wylogowania
if __name__ == "__main__":
    session = login()
    if session:
        logout(session)
