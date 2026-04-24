# permissions.py
def check_permission(user, action):
    return user.role == "admin"