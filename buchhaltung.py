import json
from tkinter import *
from tkinter.font import *
from PIL import Image, ImageTk
import time
import threading
#from plots.plot import make_plot

class Time_thread(threading.Thread):
    def __init__(self, id, name):
        threading.Thread.__init__(self)
        self.id = id
        self.name = name

    def run(self):
        print('moin')
        time.sleep(3)
        return '#202124'

wait_t = Time_thread(1, 'wait')


def show_new_plot():
    #make_plot(1, 1, None)
    return None


def open_settings():
    with open(r'user/felix/felix.json', 'r') as set:
        settings = json.load(set)
        schriftart = "Microsoft YaHei UI Light"
        # schriftart = settings["font"]
        tmp = settings["User"]["language"]
        
    lang_path = r'settings/language/' + tmp + '.json'

    with open(lang_path, 'r') as lang:
        lang_data = json.load(lang)
        lang_main_header = lang_data["headers"]["main_header"]
        lang_bar_profile = lang_data["bar"]["profile"]
        lang_bar_settings = lang_data["bar"]["settings"]
    
    sett_win = Tk()
    sett_win.title(lang_bar_settings)
    sett_win.iconbitmap(r'plots\setting.ico')
    sett_win.geometry('1000x500')
    sett_win.configure(bg='#202124')

    middel_frame= Frame(sett_win, width=300, height=900, bg='#202124')
    middel_frame.pack(fill='y')

    tmp2 = Label(middel_frame, text='Suiiii', font=(schriftart, 11))
    tmp2.pack()

    sett_win.mainloop()


def open_win(user):
    # pathh = r'user/' + user.name +'/' +user.name + '.json'
    with open(r'user/felix/felix.json', 'r') as set:
        user_set = json.load(set)
        schriftart = "Microsoft YaHei UI Light"
        # schriftart = user_set["font"]
        tmp = user_set["User"]["language"]
        
    lang_path = r'settings/language/' + tmp + '.json'

    with open(lang_path, 'r') as lang:
        lang_data = json.load(lang)
        lang_main_header = lang_data["headers"]["main_header"]
        lang_bar_profile = lang_data["bar"]["profile"]
        lang_bar_settings = lang_data["bar"]["settings"]
        lang_buttons_save = lang_data["buttons"]["save"]
        lang_buttons_plot = lang_data["buttons"]["plot"]

        # for section in lang_data:
        #     for trans in lang_data[section]:
        #         print(lang_data[section][trans])


    window = Tk()
    window.title(lang_main_header)
    window.iconbitmap(r'plots\icon.ico')
    window.geometry('2000x1000')
    window.configure(bg='#202124')



    #################################################################################################################
    '''
        Leiste
    '''

    leiste = Frame(master=window, width=268, height=3000, bg='#ffffff')
    leiste.place(x=0, y=0)

    foto_leiste = Frame(master=leiste)
    foto_leiste.place(x=0,y=0)


    # logo= PhotoImage(file=r'C:\Users\Felix\VS Code Projekts\Buchhaltung\undraw_Investing_re_bov7.png')
    width = 268
    height = 193
    img = Image.open(r"plots\undraw_Investing_re_bov7.png")
    img = img.resize((width,height), Image.Resampling.LANCZOS)
    photoImg =  ImageTk.PhotoImage(img)
    # logo.subsample(40, 40)
    # a = ImageTk.PhotoImage(logo)
    l_logo = Label(foto_leiste, image=photoImg, border=0)
    # l_logo.image = a
    l_logo.pack()


    show_prifil= Button(leiste, text=lang_bar_profile, font=(schriftart, 20), border=0, bg='#ffffff', fg='#57a1f8')
    show_prifil.place(relx=0.1, rely=0.07)

    trennung = Frame(leiste, width=220, height=5, bg='#202124')
    trennung.place(relx=0.1, rely=0.09)

    settings_prifil= Button(leiste, text=lang_bar_settings, font=(schriftart, 20), border=0, bg='#ffffff', fg='#57a1f8', command=open_settings)
    settings_prifil.place(relx=0.1, rely=0.1)

    trennung2 = Frame(leiste, width=220, height=5, bg='#202124')
    trennung2.place(relx=0.1, rely=0.12)


    ###############################################################################################################
    '''
        Main
    '''
    middel_frame= Frame(master=window, width=300, height=900, bg='#202124')
    middel_frame.pack(fill='y')

    ueberschrift = Label(middel_frame, text=lang_main_header, font=(schriftart, 30), fg='snow', bg='#202124')
    ueberschrift.pack()

    for i in range(0, 5):
        window.columnconfigure(i, weight=1, minsize=75)
        window.rowconfigure(i, weight=1, minsize=50)

    amount_in = Entry(middel_frame, width=40, font=('Consolas', 11), border=0)
    amount_in.pack(pady=5)
    amount_in.insert(0, 'Betrag')

    date_in = Entry(middel_frame, width=40, font=('Consolas', 11), border=0)
    date_in.pack(pady=5)
    date_in.insert(0, 'Date')

    info_in = Entry(middel_frame, width=40, font=('Consolas', 11), border=0)
    info_in.pack(pady=5)
    info_in.insert(0, 'Info')

    def save_input():
        amount = amount_in.get()
        amount_in.delete(0, END)
        date = date_in.get()
        date_in.delete(0, END)
        info = info_in.get()
        info_in.delete(0, END)
        print(amount, date, info)

        placeholder_l.config(text='Gespeichert', fg='#ffffff')
        
        # langsame Ausblendung, while...

    button_frame = Frame(master=middel_frame, bg='#202124')
    button_frame.pack(pady=5)

    save_button = Button(button_frame, text=lang_buttons_save, font=(schriftart, 11), border=0, command=save_input)
    # label.pack(side='left', expand=True, padx=10)
    save_button.grid(column=0, row=0)

    placeholder_l = Label(button_frame, text='Gespeichert', bg='#202124', fg='#202124')
    placeholder_l.grid(column=1, row=0)

    plot_button = Button(button_frame, text=lang_buttons_plot, font=(schriftart, 11), border=0, command=show_new_plot())
    # h_button.pack(side='right', expand=True,)
    plot_button.grid(column=2, row=0)

    graph_frame = Frame(master=middel_frame)
    graph_frame.pack()

    von_button = Entry(graph_frame, width=40, font=('Consolas', 11), border=0, fg='snow', bg='#202124', insertbackground='snow')
    von_button.pack(side='left')
    von_button.insert(0, 'Von')

    bis_button = Entry(graph_frame, width=40, font=('Consolas', 11), border=0, fg='snow', bg='#202124', insertbackground='snow')
    bis_button.pack(side='right')
    bis_button.insert(0, 'Bis')

    photo = PhotoImage(file=r'plots\first_plot.png')
    l_photo = Label(middel_frame, image=photo)
    l_photo.pack(side='bottom')


    # frame2 = Frame(window, bg='snow', width=50, height=50)
    # frame2.grid(row=3, column=3)

    window.mainloop()

open_win(None)