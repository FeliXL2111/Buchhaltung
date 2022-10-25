import sqlite3
def crate_table(table_name):
    with sqlite3.connect('employ.db') as database:
        database.execute("CREATE TABLE humans (name text, age int)")
    
def add_to_tabel(table_name, atribure_list):
    with sqlite3.connect('employ.db') as database:
        database.execute("INSERT INTO humans VALUES ('Mai', 2000)")

def print_tabel(tabel_name):
    with sqlite3.connect('employ.db') as database:
        for human in database:
            print(human)

print_tabel(None)