from sql_probe import add_to_tabel_admin, last_bankkonto_admin, last_id_admin
from user.user_class import User

def try_sql():
    id = int(input('id '))
    r_id = last_id_admin('transsaction_id') + 1
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

def try_save_user():
    u1 = User("Try")
    u1.load_tmp_for_user()
    u1.accs = 44
    u1.save_user()