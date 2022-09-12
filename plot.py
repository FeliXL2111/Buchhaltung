import matplotlib.pyplot as plt
import json

def make_plot(beginn, end):
    a = beginn
    b= end

    with open(r'user\felix\felix.json', 'r') as plot_data:
        cc = json.load(plot_data)
        for element in cc:
            print(element)
            for xx in cc[element]:
                print(xx)
                print(cc[element][xx])

        # print(cc['User']['name'])

    x = ['2022/10/10','2022/10/11','2022/10/12','2022/10/13']
    y = [1,2,3,4]

    plt.plot(x, y)
    path = r'plots\first_plot.png'
    plt.savefig(path)
    plt.show()

make_plot(1,1)