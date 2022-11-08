import sqlite3
import os


def create_table(user):
    with sqlite3.connect('../user/'+user.lower_name+'/sql_data.db') as database:
        database.execute("CREATE TABLE data (amount float, bankkonto float, day int, month int, year int, info text)")
    
def add_to_tabel(user, atribure_list):
    with sqlite3.connect('../user/'+user.lower_name+'/sql_data.db') as database:
        database.execute(f"INSERT INTO data VALUES {atribure_list}")

def print_tabel(user):
    with sqlite3.connect('../user/'+user.lower_name+'/sql_data.db') as database:
        for i in database.execute("select * from data"):
            print(i)



def create_table_admin(tmp):
    with sqlite3.connect('user/admin/sql_data.db') as database:
        database.execute("CREATE TABLE data (amount float, bankkonto float, day int, month int, year int, info text)")
    
def add_to_tabel_admin(atribure_tuple):
    with sqlite3.connect('user/admin/sql_data.db') as database:
        database.execute(f"INSERT INTO data VALUES {atribure_tuple}")

def print_tabel_admin():
    with sqlite3.connect('user/admin/sql_data.db') as database:
        for i in database.execute("select * from data"):
            print(i)

def delete_from_table_admin():
    with sqlite3.connect('user/admin/sql_data.db') as database:
        database.execute("delete from data WHERE day = 2 AND amount = 20")

def add_new_colum_admin():
    with sqlite3.connect('user/admin/sql_data.db') as database:
        database.execute("ALTER TABLE data ADD transsaction_id int")

if __name__ == '__main__':
    while True:
        sql_que = input('Gib deine Aktion an: ')
        if sql_que == 'ct':
            tmp = input('Name des table')
            create_table_admin(tmp)
        elif sql_que == 'att':
            amount = float(input('amount'))
            bankkonto = float(input('bankkonto'))
            day = int(input('day'))
            month = int(input('month'))
            year = int(input('year'))
            info = str(input('info'))
            add_to_tabel_admin()
        elif sql_que == 'pt':
            print_tabel_admin()
        elif sql_que == 'dft':
            delete_from_table_admin()
        elif sql_que == 'anc':
            add_new_colum_admin()
        elif sql_que == 'quit':
            break