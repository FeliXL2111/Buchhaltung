import matplotlib.pyplot as plt
import json

x = [1,2,3,4]
y = [4,1,4,0]

plt.plot(x, y)
path = r'C:\Users\Felix\VS Code Projekts\Buchhaltung\plots\first_plot.png'
plt.savefig(path)
plt.show()