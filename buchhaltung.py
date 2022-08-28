import json
from tkinter import *
from tkinter.font import *
from PIL import Image, ImageTk

schriftart = 'Microsoft YaHei UI Light'

window = Tk()
window.title('Buchhaltung')
window.iconbitmap('icon.ico')
window.geometry('2000x1000')
window.configure(bg='#202124')


middel_frame= Frame(master=window, width=300, height=900)
middel_frame.pack(fill='y')


leiste = Frame(master=window, width=268, height=1000, bg='#ffffff')
leiste.place(x=0, y=0)

foto_leiste = Frame(master=leiste)
foto_leiste.place(x=0,y=0)


# logo= PhotoImage(file=r'C:\Users\Felix\VS Code Projekts\Buchhaltung\undraw_Investing_re_bov7.png')
width = 268
height = 193
img = Image.open(r"C:\Users\Felix\VS Code Projekts\Buchhaltung\undraw_Investing_re_bov7.png")
img = img.resize((width,height), Image.LANCZOS)
photoImg =  ImageTk.PhotoImage(img)
# logo.subsample(40, 40)
# a = ImageTk.PhotoImage(logo)
l_logo = Label(foto_leiste, image=photoImg, border=0)
# l_logo.image = a
l_logo.pack()


show_prifil= Button(leiste, text='Profil', font=(schriftart, 20), border=0, bg='#ffffff', fg='#57a1f8')
show_prifil.place(relx=0.1, rely=0.2)


ueberschrift = Label(middel_frame, text='Überschrift', font=(schriftart, 30), fg='snow', bg='#202124')
ueberschrift.pack()

for i in range(0, 5):
    window.columnconfigure(i, weight=1, minsize=75)
    window.rowconfigure(i, weight=1, minsize=50)

box = Entry(middel_frame, width=40, font=('Consolas', 11), border=0)
box.pack()

frame = Frame(master=middel_frame)
frame.pack()

label = Label(frame, text='Hier ist ein Text', font=(schriftart, 11))
label.pack(side='right', expand=True)

label2 = Label(frame, text='Hier ist ein Dext', font=(schriftart, 11))
label2.pack(side='left',expand=True)

h_button = Button(frame, text='hinzufügen', font=(schriftart, 11), border=0, bg='blue')
h_button.pack(side='right', expand=True)

graph_frame = Frame(master=middel_frame)
graph_frame.pack()

von_button = Entry(graph_frame, width=40, font=('Consolas', 11), border=0, fg='snow', bg='#202124', insertbackground='snow')
von_button.pack(side='left')
von_button.insert(0, 'Von')

bis_button = Entry(graph_frame, width=40, font=('Consolas', 11), border=0, fg='snow', bg='#202124', insertbackground='snow')
bis_button.pack(side='right')
bis_button.insert(0, 'Bis')

photo = PhotoImage(file=r'C:\Users\Felix\VS Code Projekts\Buchhaltung\plots\first_plot.png')
l_photo = Label(middel_frame, image=photo)
l_photo.pack(side='bottom')


# frame2 = Frame(window, bg='snow', width=50, height=50)
# frame2.grid(row=3, column=3)




window.mainloop()
