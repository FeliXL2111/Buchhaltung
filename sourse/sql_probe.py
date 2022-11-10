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



def create_table_admin(tablename):
    with sqlite3.connect('user/admin/sql_data.db') as database:
        database.execute(f"CREATE TABLE {tablename} (amount float, bankkonto float, day int, month int, year int, info text)")
    
def add_to_tabel_admin(atribure_list):
    with sqlite3.connect('user/admin/sql_data.db') as database:
        database.execute(f"INSERT INTO data VALUES {atribure_list}")

def print_tabel_admin(tablename):
    with sqlite3.connect('user/admin/sql_data.db') as database:
        for i in database.execute(f"select * from {tablename}"):
            print(i)

def delete_from_table_admin():
    with sqlite3.connect('user/admin/sql_data.db') as database:
        database.execute("delete from data WHERE amount = 100")

def add_new_colum_admin():
    with sqlite3.connect('user/admin/sql_data.db') as database:
        database.execute("ALTER TABLE data ADD transsaction_id int")

def last_bankkonto(n):
    with sqlite3.connect('user/admin/sql_data.db') as database:
        for i in database.execute(f'select bankkonto from data Where transsaction_id = {n}'):
            return i

if __name__ == '__main__':
    while True:
        sql_que = input('Gib deine Aktion an: ')
        if sql_que == 'ct':
            tmp = input('Name des table')
            create_table_admin(tmp)
        if sql_que == 'att':
            id = int(input('id '))
            if id == None:
                id = 300
            amount = float(input('amount '))
            if id -1 <= 0:
                bankkonto = amount
            else:
                lb = last_bankkonto(id-1)
                bankkonto = amount + float(lb[0])
            day = int(input('day '))
            month = int(input('month '))
            year = int(input('year '))
            info = input('info ')
            full_date = input('full_date ')
            
            add_to_tabel_admin((amount, bankkonto, day, month, year, info, full_date, id))
        elif sql_que == 'pt':
            tmp = input('tablename ')
            print_tabel_admin(tmp)
        elif sql_que == 'dft':
            delete_from_table_admin()
        elif sql_que == 'anc':
            add_new_colum_admin()
        elif sql_que == 'quit':
            break