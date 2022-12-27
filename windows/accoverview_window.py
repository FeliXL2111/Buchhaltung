from tkinter import *
from tkinter.font import *
import json

def open_accoverview(user):
    global tmp_user
    tmp_user = user
    schriftart = "Microsoft YaHei UI Light"
    acc_win = Tk()
    acc_win.title('Accounts')
    acc_win.iconbitmap(r'../pic/icon.ico')
    acc_win.geometry('1000x500')
    acc_win.configure(bg='#202124')

    def add():
        tmp_user.accs.append(new_acc_in.get())
        tmp2.config(text=f'Your accounts: {user.accs}')

    def delete():
        try:
            tmp_user.accs.remove(new_acc_in.get())
            tmp2.config(text=f'Your accounts: {user.accs}')
        except:
            pass

    middel_frame= Frame(acc_win, width=300, height=900, bg='#202124')
    middel_frame.pack(fill='y')

    tmp2 = Label(middel_frame, text=f'Your accounts: {user.accs}', font=(schriftart, 11), bg='#202124', fg='snow')
    tmp2.pack()
 
    new_acc_in = Entry(middel_frame, width=40, font=('Consolas', 11), border=0)
    new_acc_in.pack(pady=0.5)

    new_acc_button = Button(middel_frame, text='Add', font=(schriftart, 11), border=0, command=add)
    new_acc_button.pack(pady=0.5)

    delet_acc_button = Button(middel_frame, text='Delete', font=(schriftart, 11), border=0, command=delete)
    delet_acc_button.pack(pady=0.5)

    acc_win.mainloop()