import time
import threading
from pynput.mouse import Button, Controller
from pynput.keyboard import Listener, KeyCode

start_end = KeyCode(char='a')
exit_key = KeyCode(char='z')

class auto_clicker_class(threading.Thread):
    def __init__(self):
        super(auto_clicker_class, self).__init__()
        self.delay = 0.0000000001
        self.button = Button.left
        self.running = False
        self.program_run = True
    def begin_clicking(self):
        self.running = True
    def clicking_stop(self):
        self.running = False
    def exit(self):
        self.clicking_stop()
        self.program_run = False
    def run(self):
        while self.program_run:
            while self.running:
                mouse_ob.click(self.button)
                time.sleep(self.delay)
            time.sleep(0.000000000001)

mouse_ob = Controller()
t = auto_clicker_class()
t.start()

def fun(k):
    if k == start_end:
        if t.running:
            t.clicking_stop()
        else:
            t.begin_clicking()
    elif k == exit_key:
        t.exit()
        listener.stop()

with Listener(on_press=fun) as listener:
    listener.join()
