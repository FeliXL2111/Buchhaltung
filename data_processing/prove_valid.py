from passwort_manager.hash_imput import hash_in
import json

def valid_user(user, username, password):
    if username == user.name and hash_in(password) == user.password:
        return True
    else:
        return False