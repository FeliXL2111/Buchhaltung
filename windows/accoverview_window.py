from tkinter import *
from tkinter.font import *
import json

def open_accoverview(user):
    global tmp_user
    tmp_user = user

    lang_path = r'../settings/language/' + tmp_user.lang + '/main_window.json'

    with open(lang_path, 'r') as lang:
        lang_data = json.load(lang)
        lang_main_header = lang_data["headers"]["main_header"]

    schriftart = "Microsoft YaHei UI Light"
    acc_win = Tk()
    acc_win.title(lang_main_header)
    acc_win.iconbitmap(r'../pic/icon.ico')
    acc_win.geometry('1000x500')
    acc_win.configure(bg='#202124')

    def add():
        #select_accs() -> implementieren in sql_probe und importieren
        tmp_user.accs += f'_{new_acc_in.get()}' #todo
        tmp_user_accs = tmp_user.accs.split('_')
        accs_list.config(text=f'Your accounts: {tmp_user_accs}')
        tmp_user.save_user()

    def delete():
        try:
            tmp_user.accs.remove(new_acc_in.get())
            accs_list.config(text=f'Your accounts: {user.accs}')
            tmp_user.save_user()
        except:
            pass

    middel_frame= Frame(acc_win, width=300, height=900, bg='#202124')
    middel_frame.pack(fill='y')

    accs_list = Label(middel_frame, text=f'Your accounts: {user.accs}', font=(schriftart, 11), bg='#202124', fg='snow')
    accs_list.pack()
 
    new_acc_in = Entry(middel_frame, width=40, font=('Consolas', 11), border=0)
    new_acc_in.pack(pady=0.5)

    new_acc_button = Button(middel_frame, text='Add', font=(schriftart, 11), border=0, command=add)
    new_acc_button.pack(pady=0.5)

    delet_acc_button = Button(middel_frame, text='Delete', font=(schriftart, 11), border=0, command=delete)
    delet_acc_button.pack(pady=0.5)

    acc_win.mainloop()