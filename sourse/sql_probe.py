import sqlite3
import os


def create_data_table(user):
    with sqlite3.connect('../user/'+user.lower_name+'/sql_data.db') as database:
        database.execute("CREATE TABLE data (amount float, bankkonto float, day int, month int, year int, info text, full_year text, transsaction_id int)")

def create_user_file(user):
    with sqlite3.connect('../user/'+user.lower_name+'/'+user.lower_name+'.db') as database:
        database.execute("CREATE TABLE user (attribut text, v text, infos text)")
        database.execute("CREATE TABLE accs (name text, created text, status text)")

    
def add_to_table(user, atribure_list):
    with sqlite3.connect('../user/'+user.lower_name+'/sql_data.db') as database:
        database.execute(f"INSERT INTO data VALUES {atribure_list}")

def add_to_user(user, atribure_list):
    with sqlite3.connect('../user/'+user.lower_name+'/'+user.lower_name+'.db') as database:
        database.execute(f"INSERT INTO user VALUES {atribure_list}")

def add_to_accs(user, atribure_list):
    with sqlite3.connect('../user/'+user.lower_name+'/'+user.lower_name+'.db') as database:
        database.execute(f"INSERT INTO accs VALUES {atribure_list}")

def change_user(user, attribut, new_v):
    with sqlite3.connect('../user/'+user.lower_name+'/'+user.lower_name+'.db') as database:
        database.execute(f"UPDATE user SET v = '{new_v}' WHERE attribut = '{attribut}'")

def print_table(user):
    with sqlite3.connect('../user/'+user.lower_name+'/sql_data.db') as database:
        for i in database.execute("select * from data"):
            print(i)

def return_table(user):
    with sqlite3.connect('../user/'+user.lower_name+'/sql_data.db') as database:
        tmp_list = []
        for i in database.execute("select * from data"):
            tmp_list.append(i)

        return tmp_list

def return_all_user_file(user, table):
    with sqlite3.connect('../user/'+user.lower_name+'/'+user.lower_name+'.db') as database:
        tmp_list = []
        for i in database.execute(f"select * from {table}"):
            tmp_list.append(i)
        return tmp_list

def return_attribut(user, column, table, attribut):
    with sqlite3.connect('../user/'+user.lower_name+'/'+user.lower_name+'.db') as database:
        for i in database.execute(f"select {column} from {table} Where attribut = '{attribut}'"):
            return i

def last_bankkonto(user, n, column):
    with sqlite3.connect('../user/'+user.lower_name+'/sql_data.db') as database:
        for i in database.execute(f'select {column} from data Where transsaction_id = {n}'):
            return i

def last_id(user, column):
    with sqlite3.connect('../user/'+user.lower_name+'/sql_data.db') as database:
        for i in database.execute(f'select MAX({column}) from data'):
            if i[0] == None:
                return 0
            else:
                return i[0]


def create_table_admin(tablename):
    with sqlite3.connect(r'../user/admin/sql_data.db') as database:
        database.execute(f"CREATE TABLE {tablename} (amount float, bankkonto float, day int, month int, year int, info text, full_year text, transsaction_id int)")
    
def add_to_tabel_admin(atribure_list):
    with sqlite3.connect(r'../user/admin/sql_data.db') as database:
        database.execute(f"INSERT INTO data VALUES {atribure_list}")

def print_tabel_admin(tablename):
    with sqlite3.connect(r'user/admin/sql_data.db') as database:
        for i in database.execute(f"select * from {tablename}"):
            print(i)

def delete_from_table_admin(n):
    with sqlite3.connect(r'../user/admin/sql_data.db') as database:
        database.execute(f"delete from data WHERE transsaction_id = {n}")

def add_new_colum_admin():
    with sqlite3.connect('user/felix/sql_data.db') as database:
        database.execute("ALTER TABLE data ADD status text")

def last_bankkonto_admin(n, column):
    with sqlite3.connect(r'../user/admin/sql_data.db') as database:
        for i in database.execute(f'select {column} from data Where transsaction_id = {n}'):
            return i

def last_id_admin(table):
    with sqlite3.connect('../user/admin/sql_data.db') as database:
        for i in database.execute(f'select MAX({table}) from data'):
            return i[0]

if __name__ == '__main__':
    while True:
        sql_que = input('Gib deine Aktion an: ')
        if sql_que == 'ct':
            tmp = input('Name des table')
            create_table_admin(tmp)
        if sql_que == 'att':
            id = int(input('id '))
            r_id = last_id_admin('transsaction_id')[0] + 1
            print(r_id)
            if id == None:
                id = 300
            amount = float(input('amount '))
            if id - 1 <= 0:
                bankkonto = amount
            else:
                lb = last_bankkonto_admin(id-1, 'bankkonto')
                bankkonto = amount + float(lb[0])
            day = int(input('day '))
            month = int(input('month '))
            year = int(input('year '))
            info = input('info ')
            full_date = str(year) + '_' + str(month) +'_' + str(day)
            
            add_to_tabel_admin((amount, bankkonto, day, month, year, info, full_date, id))
        elif sql_que == 'pt':
            tmp = input('tablename ')
            print_tabel_admin(tmp)
        elif sql_que == 'dft':
            n = input('id ')
            delete_from_table_admin(n)
        elif sql_que == 'anc':
            add_new_colum_admin()
        elif sql_que == 'quit':
            break