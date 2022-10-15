from tkinter import *
from user.user import new_user

schriftart = "Microsoft YaHei UI Light"

def tmp_new_user():
    new_user(None, None)

def open_new_user():
    window = Tk()
    window.title('Login')
    window.iconbitmap(r'..\plots\icon.ico')
    window.geometry('2000x1000')
    window.configure(bg='#202124')

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

    login = Button(window, text='Login', font=(schriftart, 20), border=0, bg='#ffffff', fg='#57a1f8', command=tmp_new_user)
    login.pack(pady=10)

    window.mainloop()