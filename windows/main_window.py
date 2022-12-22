import json
from tkinter import *
from tkinter.font import *
# from ttk import *
from PIL import Image, ImageTk
from windows.setting_window import open_settings
from windows.profile_window import open_profile
from windows.accoverview_window import open_accoverview
from windows.all_entries_window import open_all_entries
from plots.plot import make_plot
import threading
import time
from sourse.sql_probe import *

def open_win(user, xxxx = None, yyyy = None):
    global global_user
    global_user = user
    def tmp_open_settings():
        open_settings(global_user)

    def tmp_open_profile():
        open_profile(global_user)

    def tmp_open_accoverview():
        open_accoverview(global_user)

    def tmp_open_all_entries():
        open_all_entries(global_user)

    def tmp_make_plot():
        make_plot(global_user)
        return None

    pathh = r'../user/' + user.lower_name +'/' +user.lower_name + '.json'
    with open(pathh, 'r') as set:
        user_set = json.load(set)
        schriftart = "Microsoft YaHei UI Light"
        # schriftart = user_set["font"]
        tmp = user_set["user"]["language"]
        
    lang_path = r'../settings/language/' + tmp + '.json'

    with open(lang_path, 'r') as lang:
        lang_data = json.load(lang)
        lang_main_header = lang_data["headers"]["main_header"]
        lang_bar_profile = lang_data["bar"]["profile"]
        lang_bar_settings = lang_data["bar"]["settings"]
        lang_bar_kontooverview = lang_data["bar"]["accoverview"]
        lang_bar_all_prints = lang_data["bar"]["all_entries"]
        lang_buttons_save = lang_data["buttons"]["save"]
        lang_buttons_plot = lang_data["buttons"]["plot"]

        # for section in lang_data:
        #     for trans in lang_data[section]:
        #         print(lang_data[section][trans])


    window = Tk()
    window.title(lang_main_header)
    window.iconbitmap(r'../plots\icon.ico')
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


    ## logo= PhotoImage(file=r'C:\Users\Felix\VS Code Projekts\Buchhaltung\undraw_Investing_re_bov7.png')
    width = 268
    height = 193
    img = Image.open(r"../plots\undraw_Investing_re_bov7.png")
    img = img.resize((width,height), Image.Resampling.LANCZOS)
    photoImg =  ImageTk.PhotoImage(img)
    ## logo.subsample(40, 40)
    ## a = ImageTk.PhotoImage(logo)
    l_logo = Label(foto_leiste, image=photoImg, border=0)
    # l_logo.image = a
    l_logo.pack()


    show_profile= Button(leiste, text=lang_bar_profile, font=(schriftart, 20), border=0, bg='#ffffff', fg='#57a1f8', command=tmp_open_profile)
    show_profile.place(relx=0.1, rely=0.07)

    trennung = Frame(leiste, width=220, height=5, bg='#202124')
    trennung.place(relx=0.1, rely=0.09)

    settings_profile= Button(leiste, text=lang_bar_settings, font=(schriftart, 20), border=0, bg='#ffffff', fg='#57a1f8', command=tmp_open_settings)
    settings_profile.place(relx=0.1, rely=0.1)

    trennung2 = Frame(leiste, width=220, height=5, bg='#202124')
    trennung2.place(relx=0.1, rely=0.12)

    acc_overview = Button(leiste, text=lang_bar_kontooverview, font=(schriftart, 20), border=0, bg='#ffffff', fg='#57a1f8', command=tmp_open_accoverview)
    acc_overview.place(relx=0.1, rely=0.13)

    trennung3 = Frame(leiste, width=220, height=5, bg='#202124')
    trennung3.place(relx=0.1, rely=0.15)

    all_entries = Button(leiste, text=lang_bar_all_prints, font=(schriftart, 20), border=0, bg='#ffffff', fg='#57a1f8', command=tmp_open_all_entries)
    all_entries.place(relx=0.1, rely=0.16)




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
    date_in.insert(0, 'Date (Day_Month_Year)')

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
        date_split = date.split('_')
        li = last_id_admin('transsaction_id') + 1
        # user.append_data_json(amount, date, info)
        # create_table(user)
        lk = last_bankkonto_admin(li - 1, 'kontostand') + amount
        add_to_tabel(user, (amount, lk, int(date_split[0]), int(date_split[1]), int(date_split[2]), info, date, li))
        print_tabel(user)


        # placeholder_l.config(text='Gespeichert', fg='#ffffff')
        # placeholder_l.after(5000, placeholder_l.config(fg='#202124'))

    button_frame = Frame(master=middel_frame, bg='#202124')
    button_frame.pack(pady=5)

    save_button = Button(button_frame, text=lang_buttons_save, font=(schriftart, 11), border=0, command=save_input)
    # label.pack(side='left', expand=True, padx=10)
    save_button.grid(column=0, row=0)

    v = ['Acc 1', 'Acc 2']
    vs = StringVar(window)
    vs.set('Acc 1')

    acc_switch = OptionMenu(button_frame, vs,*v) #, bg='#202124', fg='#202124'
    acc_switch.grid(column=1, row=0)

    plot_image = PhotoImage(file=r'../user/'+ user.lower_name +'/'+ user.plot+'.png')
    l_photo = Label(middel_frame, image=plot_image)

    def show_new_plot():
        tmp_make_plot()
        time.sleep(0.1)
        print('plot erfolgreich gebildet')
        time.sleep(0.1)
        con_path = r'../user/'+ user.lower_name + '/'+user.plot+'.png'
        plot_image_conf = PhotoImage(file=con_path)
        l_photo.config(image=plot_image_conf)
        l_photo.image = plot_image_conf
        print('config')
        

    plot_button = Button(button_frame, text=lang_buttons_plot, font=(schriftart, 11), border=0, command=show_new_plot)
    # h_button.pack(side='right', expand=True,)                                                         lambda: threading.Thread(target=show_new_plot()).start()
    plot_button.grid(column=2, row=0)

    graph_frame = Frame(master=middel_frame)
    graph_frame.pack()

    von_button = Entry(graph_frame, width=40, font=('Consolas', 11), border=0, fg='snow', bg='#202124', insertbackground='snow')
    von_button.pack(side='left')
    von_button.insert(0, 'Von')

    bis_button = Entry(graph_frame, width=40, font=('Consolas', 11), border=0, fg='snow', bg='#202124', insertbackground='snow')
    bis_button.pack(side='right')
    bis_button.insert(0, 'Bis')

    # plot_image = PhotoImage(file=r'..\plots\first_plot.png')
    # l_photo = Label(middel_frame, image=plot_image)
    l_photo.pack(side='bottom')


    # frame2 = Frame(window, bg='snow', width=50, height=50)
    # frame2.grid(row=3, column=3)

    window.mainloop()