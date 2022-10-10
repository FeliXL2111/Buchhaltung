import json
import time
import threading
from windows.main_window import open_win
from data_processing.hash_imput import hash_in
from user import User

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

admin = User('Admin', 'adminfelix')

open_win(admin)
hash_in('Hallo')