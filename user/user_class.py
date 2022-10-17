import json
import webbrowser
import os
import time
from passwort_manager.hash_imput import hash_in

def surch(name):
    fad = r'../user/'+name+'/'+name+'.json'
    #fad = r'user'+name
    try:
        with open(fad, 'r') as file_t:
            pass
        return False
    except:
        return True


class User:
    def __init__(self, name, password):
        self.name = name
        self.lower_name = name.lower()
        self.password = hash_in(password)
        self.rank = None

    

    def load_tmp_for_user(self):
        os.makedirs(r'../user/'+ self.lower_name)
        f = open(r'../user/' + self.lower_name + '/' + self.lower_name + '.json', 'x')
        f.close()
        with open(r'../user/user_tmp/username_tmp.json', 'r') as tamplate:
            data = json.load(tamplate)

        time.sleep(0.3)

        with open(r'../user/'+ self.lower_name+ '/'+ self.lower_name+'.json', 'r+') as user_json:
            #vvv = json.load(user_json)
            #vvv.update(data)
            user_json.write(json.dumps(data, indent=4))

        time.sleep(0.3)


def new_user(name, pw):
    if surch(name):
        return User(name, pw)
    else:
        return 'already existing user'




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