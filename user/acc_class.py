import sqlite3

class Account():
    def __init__(self, user, name, created, status):
        self.user = user
        self.name = name
        self.created = created
        self.status = status

    def load_acc(self):
        pass

    def save_acc(self):
        pass