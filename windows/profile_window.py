from tkinter import *
from tkinter.font import *
import json

def open_profile(user):
    schriftart = "Microsoft YaHei UI Light"
        
    lang_path = r'../settings/language/' + user.lang + '/profile_window.json'

    with open(lang_path, 'r') as lang:
        lang_data = json.load(lang)
        lang_bar_settings = lang_data["headers"]["main_header"]
    
    pro_win = Tk()
    pro_win.title(lang_bar_settings)
    pro_win.iconbitmap(r'../pic/setting.ico')
    pro_win.geometry('1000x500')
    pro_win.configure(bg='#202124')

    middel_frame= Frame(pro_win, width=300, height=900, bg='#202124')
    middel_frame.pack(fill='y')

    username = Label(middel_frame, text=user.name, font=(schriftart, 11))
    username.pack(pady=0.5)

    rank = Label(middel_frame, text=user.rank, font=(schriftart, 11))
    rank.pack(pady=0.5)

    

    switch_password_entry = Entry(middel_frame, width=40, font=('Consolas', 11), border=0)
    switch_password_entry.pack(pady=0.5)

    def tmp_fun():
        pass #to do

    switch_password_button = Button(middel_frame, text='switch password', font=('Consolas', 11), border=0, command=tmp_fun)
    switch_password_button.pack(pady=0.5)

    pro_win.mainloop()