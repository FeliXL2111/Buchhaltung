from tkinter import *
from windows.main_window import open_win

schriftart = "Microsoft YaHei UI Light"

global world_user
world_user = None

def tmp_open_win():
    open_win(world_user)


def open_login():
    window = Tk()
    window.title('Login')
    window.iconbitmap(r'plots\icon.ico')
    window.geometry('2000x1000')
    window.configure(bg='#202124')

    ueberschrift = Label(window, text='Login', font=(schriftart, 30), fg='snow', bg='#202124')
    ueberschrift.pack()

    date_in = Entry(window, width=40, font=('Consolas', 11), border=0)
    date_in.pack(pady=5)
    date_in.insert(0, 'Username')

    trennung = Frame(window, width=220, height=5, bg='#202124')
    trennung.place()

    password_in = Entry(window, width=40, font=('Consolas', 11), border=0)
    password_in.pack(pady=5)
    password_in.insert(0, 'Password')

    trennung2 = Frame(window, width=220, height=5, bg='#202124')
    trennung2.place()

    login = Button(window, text='log in', font=(schriftart, 20), border=0, bg='#ffffff', fg='#57a1f8', command=tmp_open_win)
    login.place()

    window.mainloop()