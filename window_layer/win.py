from tkinter import *
from tkinter.font import *

def open_layerWin(user):
    def change_to_ha():
        middel_frame.pack_forget()
        hidden_frame.pack(fill='y')

    def change_to_change():
        hidden_frame.pack_forget()
        middel_frame.pack(fill='y')

    FONT = "Microsoft YaHei UI Light"    
    
    win = Tk()
    win.title('try')
    win.geometry('1000x500')
    win.configure(bg='#202124')

    list = [] #liste mit allen Frame, Buttons ect for element in list: element.pack(eigenschaften...)

    hidden_frame = Frame(win, width=300, height=900, bg='#202124')

    show_profile= Button(hidden_frame, text='Ha', font=(FONT, 20), border=0, bg='#ffffff', fg='#57a1f8', command=change_to_change)
    show_profile.pack()

    label1 = Label(hidden_frame, text='Weitertext', font=(FONT, 11), bg='#ffffff', fg='#57a1f8')
    label1.pack(pady=0.5)

    middel_frame= Frame(win, width=300, height=900, bg='#ffffff')
    middel_frame.pack(fill='y')

    tmp2 = Button(middel_frame, text='change', font=(FONT, 20), border=0, bg='#ffffff', fg='#57a1f8', command=change_to_ha)
    tmp2.pack()

    win.mainloop()

open_layerWin(4)