from hashlib import new
import json
import webbrowser

def surch(name):
    fad = r'user'+name+'/'+name+'.json'
    try:
        with open(fad, 'r') as file_t:
            pass
        return True
    except:
        return False


class User:
    def __init__(self, datei, name='Felix', password='12345'):
        self.name = name
        self.password = password
        if surch(self.name):
            pass
        else:
            self.datei = datei

webbrowser.open(r'C:\Users\Felix\VS Code Projekts\Buchhaltung\web\buch_in_web.html', new=new)
webbrowser.open(r'C:\Users\Felix\VS Code Projekts\Buchhaltung\web\in_web.html', new=new)



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