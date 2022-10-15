import matplotlib.pyplot as plt
import json
import time
global last
last = 'path_sec'

def make_plot(user, beginn = None, end = None):
    a = beginn
    b= end
    x = []
    y = []
    user_path = user.name.lower()

    with open(r'..\user\felix\data.json', 'r') as plot_data:
        cc = json.load(plot_data)
        for element in cc:
            x.append(cc[element]['date'])
            y.append(cc[element]['amount'])

        # print(cc['User']['name'])

    

    plt.plot(x, y)
    path = r'..\plots\first_plot.png'
    path_sec = r'..\plots\first_plot_sec.png'
    
    # global last

    # if last == 'path':
    plt.savefig(path_sec)     
    #     last = 'path_sec'
    # else:
    #     plt.savefig(path)
    #     last = 'path'
    plt.close()
    print(f'last: {last}')

def abfrage():
    # if chanche:
    #     return True
    # else:
    #     return False
    pass

def last_funk():
    return last