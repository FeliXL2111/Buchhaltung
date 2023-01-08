from tkinter import *
from passwort_manager.surch import surch
from user.user_class import User
from windows.main_window import open_win
from passwort_manager.hash_imput import hash_in
import time

schriftart = "Microsoft YaHei UI Light"

def open_new_user():
    window = Tk()
    window.title('Login')
    window.iconbitmap('../pic/icon.ico')
    window.geometry('2000x1000')
    window.configure(bg='#202124')

    def tmp_input():
        username = username_in.get()
        passwort = password_in.get()
        prove_passwort = prove_password_in.get()

        if passwort == prove_passwort and surch(username.lower()):
            tmp_new_user = User(username)
            tmp_new_user.load_tmp_for_user()
            tmp_new_user.load_user()
            tmp_new_user.password = hash_in(passwort)
            tmp_new_user.save_user()
            window.destroy()
            time.sleep(0.3)
            open_win(tmp_new_user)
        else:
            error_label = Label(window, text='User already exist or not the same password', font=(schriftart, 11))
            error_label.pack()

    ueberschrift = Label(window, text='New User', font=(schriftart, 30), fg='snow', bg='#202124')
    ueberschrift.pack()

    username_in = Entry(window, width=40, font=('Consolas', 11), border=0)
    username_in.pack(pady=10)
    username_in.insert(0, 'Username')

    password_in = Entry(window, width=40, font=('Consolas', 11), border=0)
    password_in.pack(pady=10)
    password_in.insert(0, 'Password')

    prove_password_in = Entry(window, width=40, font=('Consolas', 11), border=0)
    prove_password_in.pack(pady=10)
    prove_password_in.insert(0, 'repeat Password')

    login = Button(window, text='Login', font=(schriftart, 20), border=0, bg='#ffffff', fg='#57a1f8', command=tmp_input)
    login.pack(pady=10)

    window.mainloop()