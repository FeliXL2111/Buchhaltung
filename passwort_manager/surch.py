def surch(username):
    fad = r'../user/'+username+'/'+username+'.db'
    try:
        with open(fad, 'r') as file_t:
            pass
        return False
    except:
        return True