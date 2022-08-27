import json
from tkinter import *
from tkinter.font import *

schriftart = 'Microsoft YaHei UI Light'

window = Tk()
window.title('Buchhaltung')
window.iconbitmap('icon.ico')
window.geometry('2000x1000')
window.configure(bg='#202124')

def size():
    if window.winfo_height() <= 500:
        frame.place(x=100, y=100)
    else:
        frame.pack()
        l_photo.pack(padx=10, pady=10)


ueberschrift = Label(window, text='Überschrift', font=(schriftart, 30), fg='snow', bg='#202124')
ueberschrift.pack(pady = 5, padx=5)

box = Entry(window, width=40, font=('Consolas', 10), border=0)
box.pack(pady=10)

frame = Frame(master=window)
frame.pack()

label = Label(frame, text='Hier ist ein Text', font=(schriftart, 11))
label.pack()

label2 = Label(frame, text='Hier ist ein Text', font=(schriftart, 11))
label2.pack()

h_button = Button(frame, text='hinzufügen', font=(schriftart, 11), border=0, bg='blue', command=size)
h_button.pack()

photo = PhotoImage(file=r'C:\Users\Felix\VS Code Projekts\Buchhaltung\plots\first_plot.png')
l_photo = Label(window, image=photo)
l_photo.pack(padx=10, pady=10)








window.mainloop()
