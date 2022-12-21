from tkinter import *
from tkinter.font import *
import json

def open_accoverview(user):
    schriftart = "Microsoft YaHei UI Light"
    acc_win = Tk()
    acc_win.title('Acc overview')
    acc_win.iconbitmap(r'../plots\setting.ico')
    acc_win.geometry('1000x500')
    acc_win.configure(bg='#202124')

    middel_frame= Frame(acc_win, width=300, height=900, bg='#202124')
    middel_frame.pack(fill='y')

    tmp2 = Label(middel_frame, text='Suiiii', font=(schriftart, 11))
    tmp2.pack()

    acc_win.mainloop()