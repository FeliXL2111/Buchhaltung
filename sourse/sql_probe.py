import sqlite3
import os


def crate_table(table_name):
    with sqlite3.connect('user/admin/'+ table_name+'.db') as database:
        database.execute("CREATE TABLE humans (name text, age int)")
    
def add_to_tabel(table_name, atribure_list):
    with sqlite3.connect('employ.db') as database:
        database.execute(f"INSERT INTO humans VALUES {atribure_list}")

def print_tabel(tabel_name):
    with sqlite3.connect('employ.db') as database:
        for i in database.execute("select * from humans"):
            print(i)

# crate_table('name')
# add_to_tabel("humans", ("Gregor", 300))
# print_tabel(None)