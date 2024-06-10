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

# Funkcja do pobrania aktualnego użytkownika
def get_current_user(session):
    url = f"{BASE_URL}/current_user"
    response = session.get(url)
    if response.status_code == 200:
        print("Current user data:", response.json())
    else:
        print("Failed to get current user data.")
        print("Status code:", response.status_code)
        print("Response:", response.text)  # Używamy response.text dla lepszego debugowania

# Testowanie logowania i pobrania aktualnego użytkownika
if __name__ == "__main__":
    session = login()
    if session:
        get_current_user(session)
