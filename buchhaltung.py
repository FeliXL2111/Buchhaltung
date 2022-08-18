import json
from tkinter import *
from tkinter.font import *

window = Tk()
window.title('Buchhaltung')
window.iconbitmap('icon.ico')
window.geometry('1000x1000')
window.configure(bg='grey26')


photo = PhotoImage(file=r'C:\Users\Felix\VS Code Projekts\Buchhaltung\plots\first_plot.png')
l_photo = Label(window, image=photo)
l_photo.pack(pady=5)








window.mainloop()