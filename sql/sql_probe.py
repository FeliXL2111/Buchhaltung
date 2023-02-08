import sqlite3
import os


def create_data_table(user, name):
    with sqlite3.connect('../user/'+user.lower_name+'/'+ name+'.db') as database:
        database.execute("CREATE TABLE data (amount float, bankkonto float, day int, month int, year int, info text, full_year text, transsaction_id int)")

def create_user_file(user, name):
    with sqlite3.connect('../user/'+user.lower_name+'/'+name+'.db') as database:
        database.execute("CREATE TABLE user (attribut text, v text, infos text)")
        database.execute("CREATE TABLE accs (name text, created text, status text)")

    
def add_to_table(user, acc, atribure_list):
    with sqlite3.connect('../user/'+user.lower_name+'/'+acc+'.db') as database:
        database.execute(f"INSERT INTO data VALUES {atribure_list}")

def delete_from_table(user, n):
    with sqlite3.connect('../user/'+user.lower_name+'/'+user.lower_name+'.db') as database:
        database.execute(f"delete from accs WHERE name = '{n}'")

def add_to_user(user, atribure_list):
    with sqlite3.connect('../user/'+user.lower_name+'/'+user.lower_name+'.db') as database:
        database.execute(f"INSERT INTO user VALUES {atribure_list}")

def add_to_accs(user, atribure_list):
    with sqlite3.connect('../user/'+user.lower_name+'/'+user.lower_name+'.db') as database:
        database.execute(f"INSERT INTO accs VALUES {atribure_list}")

def change_user(user, attribut, new_v):
    with sqlite3.connect('../user/'+user.lower_name+'/'+user.lower_name+'.db') as database:
        database.execute(f"UPDATE user SET v = '{new_v}' WHERE attribut = '{attribut}'")

def print_table(user, name):
    with sqlite3.connect('../user/'+user.lower_name+'/'+name+'.db') as database:
        for i in database.execute("select * from data"):
            print(i)

def return_table(user, name):
    with sqlite3.connect('../user/'+user.lower_name+'/'+name+'.db') as database:
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

def last_bankkonto(user, name, n, column):
    with sqlite3.connect('../user/'+user.lower_name+'/'+name+'.db') as database:
        for i in database.execute(f'select {column} from data Where transsaction_id = {n}'):
            return i

def last_id(user, name, column):
    with sqlite3.connect('../user/'+user.lower_name+'/'+name+'.db') as database:
        for i in database.execute(f'select MAX({column}) from data'):
            if i[0] == None:
                return 0
            else:
                return i[0]


