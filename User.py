import json

def surch(name):
    fad = 'user/' + name + '.json'
    try:
        with open(fad) as file_t:
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