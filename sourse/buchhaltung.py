import threading

import sys
import os

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))


from windows.login_window import open_login
from data_processing.hash_imput import hash_in


class Time_thread(threading.Thread):
    def __init__(self, id, name, funk):
        threading.Thread.__init__(self)
        self.id = id
        self.name = name
        self.funk = funk

    def run(self):
        self.funk()

#wait_t = Time_thread(1, 'wait')


def show_new_plot():
    #make_plot(1, 1, None)
    return None

open_login()