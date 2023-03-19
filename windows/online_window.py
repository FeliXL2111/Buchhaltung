from tkinter import *
from tkinter.font import *
import json
import requests

def open_online_acc(user):

    def server():
        foo = requests.get("http://192.168.2.119:8008/user")
        print(foo)

    schriftart = "Microsoft YaHei UI Light"
        
    lang_path = r'../settings/language/' + user.lang + '/profile_window.json'

    with open(lang_path, 'r') as lang:
        lang_data = json.load(lang)
        lang_bar_settings = lang_data["headers"]["main_header"]
    
    online_win = Tk()
    online_win.title(lang_bar_settings)
    online_win.iconbitmap(r'../pic/setting.ico')
    online_win.geometry('1000x500')
    online_win.configure(bg='#202124')

    middel_frame= Frame(online_win, width=300, height=900, bg='#202124')
    middel_frame.pack(fill='y')

    username = Label(middel_frame, text='Hier ist der online abschnitt', font=(schriftart, 11))
    username.pack(pady=0.5)

    rank = Label(middel_frame, text='Das könnte mal ein button sein', font=(schriftart, 11))
    rank.pack(pady=0.5)

    

    # switch_password_entry = Entry(middel_frame, width=40, font=('Consolas', 11), border=0)
    # switch_password_entry.pack(pady=0.5)

    server_sync_button = Button(middel_frame, text='switch password', font=('Consolas', 11), border=0, command=server)
    server_sync_button.pack(pady=0.5)

    online_win.mainloop()