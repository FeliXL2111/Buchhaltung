import sqlite3
import os


def create_table(user):
    with sqlite3.connect('user/'+user.lower_name+'/sql_data.db') as database:
        database.execute("CREATE TABLE humans (name text, age int)")
    
def add_to_tabel(user, atribure_list):
    with sqlite3.connect('user/'+user.lower_name+'/sql_data.db') as database:
        database.execute(f"INSERT INTO humans VALUES {atribure_list}")

def print_tabel(user):
    with sqlite3.connect('user/'+user.lower_name+'/sql_data.db') as database:
        for i in database.execute("select * from humans"):
            print(i) 

# create_table('name')
# add_to_tabel("humans", ("Gregor", 300))
# print_tabel(None)