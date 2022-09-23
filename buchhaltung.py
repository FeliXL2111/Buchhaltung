import json
from tkinter import *
from tkinter.font import *
from PIL import Image, ImageTk

schriftart = 'Microsoft YaHei UI Light'

window = Tk()
window.title('Buchhaltung')
window.iconbitmap(r'plots\icon.ico')
window.geometry('2000x1000')
window.configure(bg='#202124')



#################################################################################################################
'''
    Liste
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


show_prifil= Button(leiste, text='Profil', font=(schriftart, 20), border=0, bg='#ffffff', fg='#57a1f8')
show_prifil.place(relx=0.1, rely=0.07)

trennung = Frame(leiste, width=220, height=5, bg='#202124')
trennung.place(relx=0.1, rely=0.09)

settings_prifil= Button(leiste, text='Einstellungen', font=(schriftart, 20), border=0, bg='#ffffff', fg='#57a1f8')
settings_prifil.place(relx=0.1, rely=0.1)

trennung2 = Frame(leiste, width=220, height=5, bg='#202124')
trennung2.place(relx=0.1, rely=0.12)


###############################################################################################################
'''
    Main
'''
middel_frame= Frame(master=window, width=300, height=900, bg='#202124')
middel_frame.pack(fill='y')

ueberschrift = Label(middel_frame, text='Buchhaltung', font=(schriftart, 30), fg='snow', bg='#202124')
ueberschrift.pack()

for i in range(0, 5):
    window.columnconfigure(i, weight=1, minsize=75)
    window.rowconfigure(i, weight=1, minsize=50)

betrag = Entry(middel_frame, width=40, font=('Consolas', 11), border=0)
betrag.pack(pady=5)
betrag.insert(0, 'Betrag')

date_in = Entry(middel_frame, width=40, font=('Consolas', 11), border=0)
date_in.pack(pady=5)
date_in.insert(0, 'Date')

info_in = Entry(middel_frame, width=40, font=('Consolas', 11), border=0)
info_in.pack(pady=5)
info_in.insert(0, 'Info')

button_frame = Frame(master=middel_frame, bg='#202124')
button_frame.pack(pady=5)

label = Button(button_frame, text='Speichern', font=(schriftart, 11), border=0)
# label.pack(side='left', expand=True, padx=10)
label.grid(column=0, row=0)

placeholder_l = Label(button_frame, text='Hello', bg='#202124', fg='#202124')
placeholder_l.grid(column=1, row=0)

h_button = Button(button_frame, text='Ploten', font=(schriftart, 11), border=0)
# h_button.pack(side='right', expand=True,)
h_button.grid(column=2, row=0)

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
