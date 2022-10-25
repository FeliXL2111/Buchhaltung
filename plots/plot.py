import matplotlib.pyplot as plt
import json

global last
last = 'path_sec'

def make_plot(user, beginn = None, end = None):
    a = beginn
    b= end
    x = []
    y = []
    user_path = user.name.lower()

    with open(r'../user/'+ user_path +'/data.json', 'r') as plot_data:
        cc = json.load(plot_data)
        for element in cc:
            x.append(cc[element]['date'])
            y.append(cc[element]['amount'])

        # print(cc['User']['name'])

    tmp_last_plot = user.plot
    if tmp_last_plot == 'first_plot':
        tmp_last_plot = 'secon_plot'
    else:
        tmp_last_plot = 'first_plot'

    plt.plot(x, y)
    path = r'../user/'+ user_path +'/'+ tmp_last_plot+'.png'
    

    plt.savefig(path)     
    plt.close()

    user.save_plot(tmp_last_plot)
    user.plot = tmp_last_plot
    print(f'last: {tmp_last_plot}, {user.plot}')

