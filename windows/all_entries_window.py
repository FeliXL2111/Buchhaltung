from tkinter import *
from tkinter.font import *
import json
from sourse.sql_probe import last_id, last_bankkonto

def open_all_entries(user):
    schriftart = "Microsoft YaHei UI Light"
    all_ent_win = Tk()
    all_ent_win.title('All Entries')
    all_ent_win.iconbitmap(r'../pic/setting.ico')
    all_ent_win.geometry('1000x500')
    all_ent_win.configure(bg='#202124')

    li = last_id(user, 'transsaction_id')
    e1 = str(last_bankkonto(user, li, '*'))
    e2 = str(last_bankkonto(user, li-1, '*'))
    e3 = str(last_bankkonto(user, li-2, '*'))
    e4 = str(last_bankkonto(user, li-3, '*'))
    e5 = str(last_bankkonto(user, li-4, '*'))

    middel_frame = Frame(all_ent_win, width=300, height=900, bg='#202124')
    middel_frame.pack(fill='y')

    entrie1 = Label(middel_frame, text=e1, font=(schriftart, 11))
    entrie1.pack()

    entrie2 = Label(middel_frame, text=e2, font=(schriftart, 11))
    entrie2.pack()

    entrie3 = Label(middel_frame, text=e3, font=(schriftart, 11))
    entrie3.pack()

    entrie4 = Label(middel_frame, text=e4, font=(schriftart, 11))
    entrie4.pack()

    entrie5 = Label(middel_frame, text=e5, font=(schriftart, 11))
    entrie5.pack()

    all_ent_win.mainloop()