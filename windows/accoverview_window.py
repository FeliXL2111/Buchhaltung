from tkinter import *
from tkinter.font import *
from tkinter import ttk
import json
from windows.account_window import open_acc_window
from windows.delete_acc_window import open_delete_acc_window

def open_accoverview(user):
    global tmp_user
    tmp_user = user

    def tmp_open_acc_window():
        open_acc_window(tmp_user, acc_selection_box.get())

    def tmp_open_delete_acc_window():
        open_delete_acc_window(tmp_user, None)

    lang_path = '../settings/language/' + tmp_user.lang + '/accoverview_window.json'

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
        # tmp_user.accs += f'_{new_acc_in.get()}' #todo
        # tmp_user_accs = tmp_user.accs.split('_')
        # accs_list.config(text=f'Your accounts: {tmp_user_accs}')
        # tmp_user.save_user()
        new_acc_b = Button(middel_frame, text=new_acc_in.get(), font=(schriftart, 11), border=0, command=open_acc_window)
        new_acc_b.pack(pady=0.5)

    def delete():
        try:
            pass
        except:
            pass

    middel_frame= Frame(acc_win, width=300, height=900, bg='#202124')
    middel_frame.pack(fill='y')

    acc_selection_box = ttk.Combobox(middel_frame, values=user.accs_names)
    acc_selection_box.pack(padx=0.5)
 
    new_acc_in = Entry(middel_frame, width=40, font=('Consolas', 11), border=0)
    new_acc_in.pack(pady=0.5)

    new_acc_button = Button(middel_frame, text='Edit', font=(schriftart, 11), border=0, command=tmp_open_acc_window)
    new_acc_button.pack(pady=0.5)

    delet_acc_button = Button(middel_frame, text='Delete', font=(schriftart, 11), border=0, command=tmp_open_delete_acc_window)
    delet_acc_button.pack(pady=0.5)

    acc_win.mainloop()