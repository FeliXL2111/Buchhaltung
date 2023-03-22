from tkinter import *
from tkinter.font import *

def open_layerWin(user):

    DARK = '#202124'
    WHITE = '#ffffff'

    def change_to_profil():
        middel_frame.pack_forget()
        hidden_frame.pack(fill='y')
        button2_home_frame.config(bg=DARK)
        tmp3.config(bg=DARK)
        button1_home_frame.config(bg=WHITE)
        tmp2.config(bg=WHITE)

    def change_to_change():
        hidden_frame.pack_forget()
        middel_frame.pack(fill='y')
        button1_home_frame.config(bg=DARK)
        tmp2.config(bg=DARK)
        button2_home_frame.config(bg=WHITE)
        tmp3.config(bg=WHITE)

    def check_height(event):
        winHeight = event.width
        winWidth = event.height/2
        leiste_frame.config(height=winHeight)

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




    leiste_frame= Frame(win, width=300, height=win.winfo_screenheight(), bg='#ffffff')
    leiste_frame.place(x=0,y=0)

    button1_home_frame= Frame(leiste_frame, width=300, height=60, bg='#202124', border=4, borderwidth=4)
    button1_home_frame.place(rely=0.1)
    tmp2 = Button(leiste_frame, text='Home', font=(FONT, 20), border=0, bg='#202124', fg='#57a1f8', command=change_to_change)
    tmp2.place(relx=0.1, rely=0.1)

    button2_home_frame= Frame(leiste_frame, width=300, height=60, bg='#ffffff')
    button2_home_frame.place(rely=0.2)
    tmp3 = Button(leiste_frame, text='Profil', font=(FONT, 20), border=0, bg='#ffffff', fg='#57a1f8', command=change_to_profil)
    tmp3.place(relx=0.1, rely=0.2)

    middel_frame= Frame(win, width=300, height=900, bg='#ffffff')
    middel_frame.pack(fill='y')

    middel_label = Label(middel_frame, text='Moin')
    middel_label.pack()

    # win.bind("<Configure>", check_height)
    win.mainloop()

open_layerWin(4)