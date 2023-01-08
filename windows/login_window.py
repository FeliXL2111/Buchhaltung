from tkinter import *
from windows.main_window import open_win
from windows.new_user_window import open_new_user
from user.user_class import User
import time
from data_processing.prove_valid import valid_user
from passwort_manager.surch import surch

schriftart = "Microsoft YaHei UI Light"


def tmp_open_win(u):
    open_win(u)



def open_login():
    window = Tk()
    window.title('Login')
    window.iconbitmap('../pic/icon.ico')
    window.geometry('2000x1000')
    window.configure(bg='#202124')

    def tmp_open_new_user():
        window.destroy()
        time.sleep(0.3)
        open_new_user()

    def tmp_imput_prove():
        username = username_in.get()
        password = password_in.get()
        if not surch(username.lower()):
            userrr = User(username, None)
            userrr.load_user()
            if valid_user(userrr, username, password):
                window.destroy()
                time.sleep(0.3)
                tmp_open_win(userrr)
            else:
                invalid_label = Label(window, text='No valid inputs')
                invalid_label.pack()
        else:
            nouser_label = Label(window, text='No User found')
            nouser_label.pack()


    ueberschrift = Label(window, text='Login', font=(schriftart, 30), fg='snow', bg='#202124')
    ueberschrift.pack()

    username_in = Entry(window, width=40, font=('Consolas', 11), border=0)
    username_in.pack(pady=10)
    username_in.insert(0, 'Username')

    password_in = Entry(window, width=40, font=('Consolas', 11), border=0, show='*')
    password_in.pack(pady=10)
    password_in.insert(0, 'Password')

    login = Button(window, text='Login', font=(schriftart, 20), border=0, bg='#ffffff', fg='#57a1f8', command=tmp_imput_prove)
    login.pack(pady=10)

    login = Button(window, text='New User', font=(schriftart, 20), border=0, bg='#ffffff', fg='#57a1f8', command=tmp_open_new_user)
    login.pack(pady=10)

    window.mainloop()