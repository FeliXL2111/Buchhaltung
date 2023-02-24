import threading

import sys
import os

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))


from windows.login_window import open_login

# import customtkinter

class Thread(threading.Thread):
    def __init__(self, id, name, funk):
        threading.Thread.__init__(self)
        self.id = id
        self.name = name
        self.funk = funk

    def run(self):
        self.funk()

def backend_funk():
    #sys.cmd(bachend.exe)

if __name__ == '__main__':
    window_thread = Thread(1, 'window', open_login)
    backend_thread = Thread(2, 'backend', backend_funk)
    window_thread.run()
    backend_thread.run()
