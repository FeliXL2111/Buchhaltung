def test_date(date):
    try:
        x = 1
        return True 
    except:
        return False

def test_info(info):
    try:
        tested_info = str(info)
        return True
    except:
        return False

def test_amount(amount):
    try:
        tested_amount = float(amount)
        return True 
    except:
        return False

def test_input_accuracy(amount, date, info):
    if test_amount(amount) and test_date(date) and test_info(info):
        return 'ok'
        # save_funk(amount, date, info)
    else:
        return 'No accurat inputs'

print(test_input_accuracy(300, 30_11_3030, 'Datto'))