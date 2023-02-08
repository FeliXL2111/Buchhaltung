from tkinter import *
from tkinter.font import *
import json
from sql.sql_probe import last_id, last_bankkonto

def open_all_entries(user):

    def back():
        e1 = str(last_bankkonto(user, 'main', li, '*'))
        e2 = str(last_bankkonto(user, 'main', li-1, '*'))
        e3 = str(last_bankkonto(user, 'main', li-2, '*'))
        e4 = str(last_bankkonto(user, 'main', li-3, '*'))
        e5 = str(last_bankkonto(user, 'main', li-4, '*'))

        entrie1.config(text=e2)
        entrie2.config(text=e3)

    def forward():
        pass

    schriftart = "Microsoft YaHei UI Light"
    all_ent_win = Tk()
    all_ent_win.title('All Entries')
    all_ent_win.iconbitmap(r'../pic/setting.ico')
    all_ent_win.geometry('1000x500')
    all_ent_win.configure(bg='#202124')

    li = last_id(user, 'main', 'transsaction_id')
    e1 = str(last_bankkonto(user, 'main', li, '*'))
    e2 = str(last_bankkonto(user, 'main', li-1, '*'))
    e3 = str(last_bankkonto(user, 'main', li-2, '*'))
    e4 = str(last_bankkonto(user, 'main', li-3, '*'))
    e5 = str(last_bankkonto(user, 'main', li-4, '*'))

    middel_frame = Frame(all_ent_win, width=300, height=900, bg='#202124')
    middel_frame.pack(fill='y')

    entrie1 = Label(middel_frame, text=e1, font=(schriftart, 11))
    entrie1.pack(pady=0.5)

    entrie2 = Label(middel_frame, text=e2, font=(schriftart, 11))
    entrie2.pack(pady=0.5)

    entrie3 = Label(middel_frame, text=e3, font=(schriftart, 11))
    entrie3.pack(pady=0.5)

    entrie4 = Label(middel_frame, text=e4, font=(schriftart, 11))
    entrie4.pack(pady=0.5)

    entrie5 = Label(middel_frame, text=e5, font=(schriftart, 11))
    entrie5.pack(pady=0.5)

    back_button = Button(middel_frame, text='<- Back', font=(schriftart, 11), border=0, command=back)
    back_button.pack(pady=0.5)

    forward_button = Button(middel_frame, text='Forward ->', font=(schriftart, 11), border=0, command=forward)
    forward_button.pack(pady=0.5)

    all_ent_win.mainloop()