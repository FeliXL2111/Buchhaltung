from tkinter import *
from tkinter.font import *
import json

def open_acc_window(user, acc):
    lang_path = r'../settings/language/' + user.lang + '/account_window.json'
    schriftart = "Microsoft YaHei UI Light"
    with open(lang_path, 'r') as lang:
        lang_data = json.load(lang)
        lang_main_header = lang_data["headers"]["main_header"]
        lang_bar_settings = lang_data["other"]["ok"]
    
    sett_win = Tk()
    sett_win.title(lang_bar_settings)
    sett_win.iconbitmap(r'../pic/setting.ico')
    sett_win.geometry('1000x500')
    sett_win.configure(bg='#202124')

    def ok():
        pass

    middel_frame= Frame(sett_win, width=300, height=900, bg='#202124')
    middel_frame.pack(fill='y')

    acc_name = Label(middel_frame, text=acc, font=(schriftart, 11))
    acc_name.pack(pady=0.5)

    acc_created = Label(middel_frame, text=acc, font=(schriftart, 11))
    acc_created.pack(pady=0.5)

    acc_delete = Button(middel_frame,  text='Delete', font=(schriftart, 11), border=0, command=ok)
    acc_delete.pack(pady=0.5)

    sett_win.mainloop()