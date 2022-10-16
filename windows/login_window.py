from tkinter import *
from windows.main_window import open_win
from windows.new_user_window import open_new_user
from user.user_class import User
import time
from data_processing.prove_valid import valid_user

schriftart = "Microsoft YaHei UI Light"

global world_user
world_user = User('Admin', 'adminfelix')

global admin_boo
admin_boo = False

def tmp_open_win():
    open_win(world_user)



def open_login():
    window = Tk()
    window.title('Login')
    window.iconbitmap(r'..\plots\icon.ico')
    window.geometry('2000x1000')
    window.configure(bg='#202124')

    def tmp_open_new_user():
        window.destroy()
        time.sleep(0.5)
        open_new_user()

    def tmp_imput_prove():
        username = username_in.get()
        password = password_in.get()
        if valid_user(username, password):
            window.destroy()
            time.sleep(0.5)
            tmp_open_win()
        else:
            invalid_label = Label(window, text='No valid inputs')
            invalid_label.pack()


    ueberschrift = Label(window, text='Login', font=(schriftart, 30), fg='snow', bg='#202124')
    ueberschrift.pack()

    username_in = Entry(window, width=40, font=('Consolas', 11), border=0)
    username_in.pack(pady=10)
    username_in.insert(0, 'Username')

    password_in = Entry(window, width=40, font=('Consolas', 11), border=0)
    password_in.pack(pady=10)
    password_in.insert(0, 'Password')

    login = Button(window, text='Login', font=(schriftart, 20), border=0, bg='#ffffff', fg='#57a1f8', command=tmp_imput_prove)
    login.pack(pady=10)

    login = Button(window, text='New User', font=(schriftart, 20), border=0, bg='#ffffff', fg='#57a1f8', command=tmp_open_new_user)
    login.pack(pady=10)

    window.mainloop()