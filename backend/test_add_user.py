import requests

url = "http://localhost:8000/user/"

# Dane nowego użytkownika
new_user = {
    "username": "testuser",
    "email": "testuser@example.com",
    "password": "password123"
}

response = requests.post(url, json=new_user)

if response.status_code == 200:
    print("Użytkownik został pomyślnie dodany.")
    print("Response:", response.json())
else:
    print("Błąd podczas dodawania użytkownika.")
    print("Status code:", response.status_code)
    print("Response:", response.text)
