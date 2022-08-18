import json
from tkinter import *
from tkinter.font import *

schriftart = 'Consolas'

window = Tk()
window.title('Buchhaltung')
window.iconbitmap('icon.ico')
window.geometry('2000x1000')
window.configure(bg='grey26')





ueberschrift = Label(window, text='Überschrift', font=(schriftart, 30), bg='snow')
ueberschrift.pack(pady = 5, fill='x', padx=5)

box = Entry(window, width=40)
box.place(x=700,y=90)

frame = Frame(master=window)
frame.place(x=1000, y=70)

label = Label(frame, text='Hier ist wein Text', font=(schriftart, 10))
label.pack()

photo = PhotoImage(file=r'C:\Users\Felix\VS Code Projekts\Buchhaltung\plots\first_plot.png')
l_photo = Label(window, image=photo)
l_photo.place(x=20, y=70)








window.mainloop()