import json
from tkinter import *
from tkinter.font import *

schriftart = 'Times'

window = Tk()
window.title('Buchhaltung')
window.iconbitmap('icon.ico')
window.geometry('2000x1000')
window.configure(bg='#202124')





ueberschrift = Label(window, text='Überschrift', font=(schriftart, 30), fg='snow', bg='#202124')
ueberschrift.pack(pady = 5, padx=5)

box = Entry(window, width=40, font=('Consolas', 10))
box.pack(pady=10)

frame = Frame(master=window)
frame.pack()

label = Label(frame, text='Hier ist ein Text', font=(schriftart, 10))
label.grid(row=0, column=0)

label2 = Label(frame, text='Hier ist ein Text', font=(schriftart, 10))
label2.grid(row=1, column=1)

photo = PhotoImage(file=r'C:\Users\Felix\VS Code Projekts\Buchhaltung\plots\first_plot.png')
l_photo = Label(window, image=photo)
l_photo.pack(padx=10, pady=10)








window.mainloop()
