import matplotlib.pyplot as plt
import json
import sqlite3

def make_plot(user, beginn = None, end = None):
    a = beginn
    b= end
    x = []
    y = []
    user_path = user.name.lower()

    # with open(r'../user/'+ user_path +'/data.json', 'r') as plot_data:
    #     cc = json.load(plot_data)
    #     for element in cc:
    #         x.append(cc[element]['date'])
    #         y.append(cc[element]['amount'])

        # print(cc['User']['name'])

    with sqlite3.connect('../user/'+user.lower_name+'/sql_data.db') as database:
        for i in database.execute("select * from data"):
            x.append(i[6])
            y.append(i[0])

    tmp_last_plot = user.plot
    if tmp_last_plot == 'first_plot':
        tmp_last_plot = 'secon_plot'
    else:
        tmp_last_plot = 'first_plot'

    plt.plot(x, y)
    path = r'../user/'+ user_path +'/'+ tmp_last_plot+'.png'
    
    print('ok 1')
    plt.savefig(path)     
    plt.close()

    print('ok 2')
    user.save_plot(tmp_last_plot)
    user.plot = tmp_last_plot
    print(f'last: {tmp_last_plot}, {user.plot}')

