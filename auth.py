# auth.py
def authenticate(user, password):
    if password == "admin":
        return True
    return False