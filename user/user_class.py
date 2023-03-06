import json
import webbrowser
import os
from datetime import date
from passwort_manager.hash_imput import hash_in
from sql.sql_probe import *
from user.acc_class import Account
from plots.plot import make_plot


class User:
    def __init__(self, name, password=None):
        self.name = name
        self.lower_name = name.lower()
        self.password = password
        self.rank = None
        self.lang = None
        self.plot = None
        self.accs = []
        self.accs_names = []

    
    
    def load_user(self):
        self.rank = return_attribut(self, 'v', 'user', 'rank')[0]
        self.lang = return_attribut(self, 'v', 'user', 'lang')[0]
        self.plot = return_attribut(self, 'v', 'user', 'plot')[0]
        self.password = return_attribut(self, 'v', 'user', 'password')[0]
        self.accs = []
        self.accs_names = []
        accs = return_all_user_file(self, 'accs')
        print(accs, 'hier')
        for i in accs:
            print(i)
            self.accs.append(Account(self, i[0], i[1], i[2]))
        print(self.accs)
        tmp_list = []
        for i in self.accs:
            print(i)
            tmp_list.append(i.name)
        print(tmp_list)
        self.accs_names = tmp_list


    def save_user(self):
        # for i in self.accs:
        #     i.save_acc(self)
        change_user(self, 'password', self.password)


    def load_tmp_for_user(self):
        os.makedirs('../user/'+ self.lower_name)
        os.makedirs('../user/'+self.lower_name+'/pdf')
        create_user_file(self, 'changes')

        create_user_file(self, self.lower_name)
        create_data_table(self, 'main')
        add_to_user(self, ('name', '0', '0'))
        add_to_user(self, ('lower_name', '0', '0'))
        add_to_user(self, ('password', '0', '0'))
        add_to_user(self, ('lang', 'english', '0'))
        add_to_user(self, ('rank', 'user', '0'))
        add_to_user(self, ('accs', '1', '0'))
        add_to_user(self, ('plot', 'first_plot', '0'))

        add_to_accs(self, ('main', '01_01_2023', 'real'))

        make_plot(self, "Konto", 'main')

    def save_plot(self, last_plot):
        change_user(self, 'plot', last_plot)


    def append_data_json(self, amount, date, info):
        with open(r'../user/'+ self.lower_name +'/data.json', 'r+') as raw_append_data:
            convert_append_data = json.load(raw_append_data)
            tmp = {"paymentx": {"amount": amount,"money": 210,"date": date,"reason": info}}
            convert_append_data["paymentx"] = tmp
            #raw_append_data.write(json.dump(convert_append_data, raw_append_data, indent=4))
            convert_append_data.update(convert_append_data, indent=4)
            json.dump(convert_append_data, raw_append_data)

    def append_data_sql(self, amount, date, info):
        add_to_table(self.lower_name, (amount, date, info))

    def new_acc(self, new_name, status):
        for i in self.accs_names:
            if i != new_name:
                pass
            else:
                print('nope, user_class.new_acc zeile 87')
                return 1
        today = str(date.today()).split('-')
        t_l = f'{today[2]}_{today[1]}_{today[0]}'
        add_to_accs(self, (new_name, t_l, status))
        self.accs.append(Account(self, new_name, t_l, status))

    def print_data(self, name):
        print_table(self, name)

    def return_acc_names(self):
        tmp_list = []
        for i in self.accs:
            tmp_list.append(i.name)
        print(tmp_list)
        return tmp_list

    def return_acc(self, acc_name):
        for acc in self.accs:
            if acc.name == acc_name:
                return acc
        return False

    def update(self):
        pass

    def save(self):
        pass

    def server_sync(self):
        pass
    
    def make_pdf(self, name = 'main'):
        x = []
        with sqlite3.connect('../user/'+self.lower_name+'/'+name+'.db') as database:
            for i in database.execute("select * from data"):
                x.append([i[0],i[1],i[2],i[3],i[4],i[5],i[6]])
        print(x)
        with open('../user/user_tmp/pdf_tmp.tex', 'r') as f:
            tmp = f.read()
        with open('../user/'+self.lower_name+'/pdf/list.tex', 'w') as file:
            file.write(tmp)
            for n in x:
                file.writelines(f'{str(n[0])} & {str(n[1])} & {str(n[2])} & {str(n[3])} & {str(n[4])} & {str(n[5])} & {str(n[0])} \\\ \n')
                file.writelines('\hline\n')
                # for m in n:
                #     file.writelines(str(m))
            file.writelines('\end'+'{'+'tabular}\n')
            file.writelines('\end'+'{'+'table}\n')
            file.writelines('\end'+'{'+'dokument}')
        print(os.getcwd())
        e = {os.path.abspath('../user/'+self.lower_name+'/pdf')}
        os.chdir(os.path.abspath('../user/'+self.lower_name+'/pdf'))
        print(str(e))
        os.system(f'latex  -recorder  "list.tex"') #{os.path.abspath('..')}
        print(os.path, 'ok')
        print(os.path.abspath('..'))


# webbrowser.open(r'C:\Users\Felix\VS Code Projekts\Buchhaltung\web\buch_in_web.html', new=new)
# webbrowser.open(r'C:\Users\Felix\VS Code Projekts\Buchhaltung\web\in_web.html', new=new)


# user1 = User('user/felix.json', 'Felix', 'xxxxxx')
# d1 = user1.datei
# n1 = user1.name
# p1 = user1.password

# with open('user/felix.json') as luser_datei:
#     data = json.load(luser_datei)

# data["User"]["datei"] = d1
# data["User"]["name"] = n1
# data["User"]["password"] = p1

# with open('user/felix.json', 'w') as user_datei:
#     user_datei.write(json.dumps(data, indent=4))
# kommentae