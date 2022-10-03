import json
from tkinter import *
from tkinter.font import *
from PIL import Image, ImageTk
import time
import threading
from windows.main_window import open_win

class Time_thread(threading.Thread):
    def __init__(self, id, name):
        threading.Thread.__init__(self)
        self.id = id
        self.name = name

    def run(self):
        print('moin')
        time.sleep(3)
        return '#202124'

#wait_t = Time_thread(1, 'wait')


def show_new_plot():
    #make_plot(1, 1, None)
    return None


# width = 268
# height = 193
# img = Image.open(r"plots\undraw_Investing_re_bov7.png")
# img = img.resize((width,height), Image.Resampling.LANCZOS)
# logo_img =  ImageTk.PhotoImage(img)

# time.sleep(3)

# photo = PhotoImage(file=r'plots\first_plot.png')

open_win(None, None, None)