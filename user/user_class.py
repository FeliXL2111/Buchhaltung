import json
import webbrowser
import os
import time
from passwort_manager.hash_imput import hash_in
from sourse.sql_probe import *
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
        accs = return_all_user_file(self, 'accs')
        print(accs, 'hier')
        for i in accs:
            print(i)
            self.accs.append(Account(self, i[0], i[1]))
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

        create_user_file(self)
        create_data_table(self)
        add_to_user(self, ('name', '0', '0'))
        add_to_user(self, ('lower_name', '0', '0'))
        add_to_user(self, ('password', '0', '0'))
        add_to_user(self, ('lang', 'english', '0'))
        add_to_user(self, ('rank', 'user', '0'))
        add_to_user(self, ('accs', '1', '0'))
        add_to_user(self, ('plot', 'first_plot', '0'))

        add_to_accs(self, ('main', '01_01_2023', 'real'))

        make_plot(self)

    def save_plot(self, last_plot):
        with open(r'../user/'+ self.lower_name +'/'+ self.lower_name +'.json', 'r+') as last_plot_data:
            dada = json.load(last_plot_data)
            dada["data_stats"]["last_plot"] = last_plot
        with open(r'../user/'+ self.lower_name +'/'+ self.lower_name +'.json', 'r+') as last_plot_data_2:
            json.dump(dada, last_plot_data_2, indent=4)


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

    def print_data(self):
        print_table(self)

    def return_acc_names(self):
            tmp_list = []
            for i in self.accs:
                tmp_list.append(i.name)
            print(tmp_list)
            return tmp_list

    



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