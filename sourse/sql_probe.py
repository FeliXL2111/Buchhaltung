import sqlite3
import os


def create_table(user, table_name):
    with sqlite3.connect('user/'+user.lower_name+'/'+ table_name+'.db') as database:
        database.execute("CREATE TABLE humans (name text, age int)")
    
def add_to_tabel(table_name, atribure_list):
    with sqlite3.connect('employ.db') as database:
        database.execute(f"INSERT INTO humans VALUES {atribure_list}")

def print_tabel(tabel_name):
    with sqlite3.connect('employ.db') as database:
        for i in database.execute("select * from humans"):
            print(i)

# create_table('name')
# add_to_tabel("humans", ("Gregor", 300))
# print_tabel(None)