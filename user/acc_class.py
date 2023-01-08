import sqlite3

class Account():
    def __init__(self, user, name, created):
        self.user = user
        self.name = name
        self.created = created

    def load_acc(self):
        pass

    def save_acc(self):
        pass