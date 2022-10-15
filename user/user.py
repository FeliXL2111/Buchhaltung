import json
import webbrowser

def surch(name):
    # fad = r'user'+name+'/'+name+'.json'
    fad = r'user'+name
    try:
        with open(fad, 'r') as file_t:
            pass
        return False
    except:
        return True


class User:
    def __init__(self, name='Felix', password='12345'):
        self.name = name
        self.lower_name = name.lower()
        self.password = password
        self.rank = None

# webbrowser.open(r'C:\Users\Felix\VS Code Projekts\Buchhaltung\web\buch_in_web.html', new=new)
# webbrowser.open(r'C:\Users\Felix\VS Code Projekts\Buchhaltung\web\in_web.html', new=new)

def new_user(name, pw):
    if surch(name):
        # user = User(name, pw)
        return 'x'
    else:
        return 'already existing user'


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