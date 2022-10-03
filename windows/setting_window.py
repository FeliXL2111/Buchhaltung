from tkinter import *
from tkinter.font import *
import json

def open_settings(user):
    with open(r'user/felix/felix.json', 'r') as set:
        settings = json.load(set)
        schriftart = "Microsoft YaHei UI Light"
        # schriftart = settings["font"]
        tmp = settings["user"]["language"]
        
    lang_path = r'settings/language/' + tmp + '.json'

    with open(lang_path, 'r') as lang:
        lang_data = json.load(lang)
        lang_main_header = lang_data["headers"]["main_header"]
        lang_bar_profile = lang_data["bar"]["profile"]
        lang_bar_settings = lang_data["bar"]["settings"]
    
    sett_win = Tk()
    sett_win.title(lang_bar_settings)
    sett_win.iconbitmap(r'plots\setting.ico')
    sett_win.geometry('1000x500')
    sett_win.configure(bg='#202124')

    middel_frame= Frame(sett_win, width=300, height=900, bg='#202124')
    middel_frame.pack(fill='y')

    tmp2 = Label(middel_frame, text='Suiiii', font=(schriftart, 11))
    tmp2.pack()

    sett_win.mainloop()