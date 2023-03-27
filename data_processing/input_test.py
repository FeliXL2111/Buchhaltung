def test_date(date) -> bool:
    
    try:
        arr = date.split('_')
        print(arr)
        return True 
    except:
        return False

def test_info(info) -> bool:
    try:
        tested_info = str(info)
        return True
    except:
        return False

def test_amount(amount) -> bool:
    try:
        tested_amount = float(amount)
        return True 
    except:
        return False

def test_input_accuracy(amount, date, info) -> str:
    if test_amount(amount) and test_date(date) and test_info(info):
        return 'ok'
        # save_funk(amount, date, info)
    else:
        return 'No accurat inputs'
