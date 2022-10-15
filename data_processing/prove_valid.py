from passwort_manager.hash_imput import hash_in

def valid_user(username, password):
    if username == 'Admin' and hash_in(password) == '4eb4ee0e23c5f4248ea217e6c039aaffc159c8405eaeb8ad16b84bfeb9cd20cfdfe8b5aacaa326f801cd5c750c843617809d84e25e2655cb991041b7cf06a212':
        return True
    else:
        return False