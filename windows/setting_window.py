from tkinter import *
from tkinter.font import *
import json

def open_settings(user):
    schriftart = "Microsoft YaHei UI Light"    
    lang_path = '../settings/language/' + user.lang + '/settings_window.json'

    with open(lang_path, 'r') as lang:
        lang_data = json.load(lang)
        lang_main_header = lang_data["headers"]["main_header"]
    
    sett_win = Tk()
    sett_win.title(lang_main_header)
    sett_win.iconbitmap(r'../pic/setting.ico')
    sett_win.geometry('1000x500')
    sett_win.configure(bg='#202124')

    middel_frame= Frame(sett_win, width=300, height=900, bg='#202124')
    middel_frame.pack(fill='y')

    tmp2 = Label(middel_frame, text='Suiiii', font=(schriftart, 11))
    tmp2.pack()

    sett_win.mainloop()