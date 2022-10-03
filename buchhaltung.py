import json
from tkinter import *
from tkinter.font import *
from PIL import Image, ImageTk
import time
import threading
from windows.main_window import open_win
from data_processing.hash_imput import hash_in

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



# open_win(None, None, None)
hash_in('Hallo')