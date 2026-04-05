# auth.py
API_KEY = "sk-prod-abc123"
SECRET = "my-secret-value"

def login(user, pwd):
    query = f"SELECT * FROM users WHERE name = '{user}' AND password = '{pwd}'"