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
        open_acc_window(tmp_user, tmp_user.return_acc(acc_selection_box.get()))

    def tmp_user_new_acc_window():
        # tmp_user.new_acc(acc_selection_box.get(), real_virtual_selection_box.get())
        # acc_selection_box.delete(0, END)
        # real_virtual_selection_box.delete(0, END)
        middel_frame.pack_forget()
        middel_frame_new_acc.pack(fill='y')

    def back():
        middel_frame_new_acc.pack_forget()
        middel_frame.pack(fill='y')

    def tmp_add_acc():
        tmp_user.new_acc(acc_name_box_new_acc.get(), real_virtual_selection_box_new_acc.get())
        acc_name_box_new_acc.delete(0, END)
        real_virtual_selection_box_new_acc.delete(0, END)

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
        pass

    def delete():
        try:
            pass
        except:
            pass

    middel_frame= Frame(acc_win, width=300, height=900, bg='#202124')
    middel_frame.pack(fill='y')

    acc_selection_box = ttk.Combobox(middel_frame, values=user.accs_names)
    acc_selection_box.pack(pady=0.5)

    r_v = ['real', 'virtual']

    real_virtual_selection_box = ttk.Combobox(middel_frame, values=r_v)
    real_virtual_selection_box.pack(pady=0.5)

    edit_acc_button = Button(middel_frame, text='Edit', font=(schriftart, 11), border=0, command=tmp_open_acc_window)
    edit_acc_button.pack(pady=0.5)

    new_acc_button = Button(middel_frame, text='New Acc', font=(schriftart, 11), border=0, command=tmp_user_new_acc_window)
    new_acc_button.pack(pady=0.5)

    pdf_button = Button(middel_frame, text='Make pdf', font=(schriftart, 11), border=0, command=user.make_pdf)
    pdf_button.pack(pady=2, padx=4)

    diccc = {
        'hallo':tmp_user_new_acc_window
    }

    tryy = ttk.OptionMenu(middel_frame, variable=r_v)
    tryy.pack(pady=2)

    tryy2 = ttk.Menubutton(middel_frame, menu=Menu(cnf=diccc))
    tryy2.pac(pady=2)

    middel_frame_new_acc= Frame(acc_win, width=300, height=900, bg='#202124')
    
    acc_name_box_new_acc = Entry(middel_frame_new_acc, font=('Consolas', 11), border=0)
    acc_name_box_new_acc.pack(pady=0.5)

    real_virtual_selection_box_new_acc = ttk.Combobox(middel_frame_new_acc, values=r_v)
    real_virtual_selection_box_new_acc.pack(pady=0.5)

    edit_acc_button_new_acc = Button(middel_frame_new_acc, text='Add', font=(schriftart, 11), border=0, command=tmp_add_acc)
    edit_acc_button_new_acc.pack(pady=0.5)

    new_acc_button_new_acc = Button(middel_frame_new_acc, text='Cancel', font=(schriftart, 11), border=0, command=back)
    new_acc_button_new_acc.pack(pady=0.5)

    acc_win.mainloop()