from tkinter import *
from tkinter.font import *
import json
from sql.sql_probe import last_id, last_bankkonto

def open_all_entries(user):
    global li
    li = last_id(user, 'main', 'transsaction_id')

    def back():
        global li
        li -= 1
        change_tabel(li)

    def forward():
        global li
        li += 1
        change_tabel(li)

    def change_tabel(li_tmp):
        e1 = str(last_bankkonto(user, 'main', li_tmp, '*'))
        e3 = str(last_bankkonto(user, 'main', li_tmp-2, '*'))
        e4 = str(last_bankkonto(user, 'main', li_tmp-3, '*'))
        e5 = str(last_bankkonto(user, 'main', li_tmp-4, '*'))
        e2 = str(last_bankkonto(user, 'main', li_tmp-1, '*'))

        entrie1.config(text=e1)
        entrie2.config(text=e2)
        entrie3.config(text=e3)
        entrie4.config(text=e4)
        entrie5.config(text=e5)

    schriftart = "Microsoft YaHei UI Light"
    all_ent_win = Tk()
    all_ent_win.title('All Entries')
    all_ent_win.iconbitmap(r'../pic/setting.ico')
    all_ent_win.geometry('1000x500')
    all_ent_win.configure(bg='#202124')

    
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