from passwort_manager.hash_imput import hash_in

def valid_user(user, username, password) -> bool:
    if username == user.name and hash_in(password) == user.password:
        return True
    else:
        return False