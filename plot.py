import matplotlib.pyplot as plt
import json

def make_plot(beginn, end, user):
    a = beginn
    b= end
    x = []
    y = []
    # user_path = user.name.lower()

    with open(r'user\felix\data.json', 'r') as plot_data:
        cc = json.load(plot_data)
        for element in cc:
            x.append(cc[element]['date'])
            y.append(cc[element]['amount'])

        # print(cc['User']['name'])


    plt.plot(x, y)
    path = r'plots\first_plot.png'
    plt.savefig(path)
    plt.show()

make_plot(1,1,None)