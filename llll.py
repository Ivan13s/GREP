import importlib
import random
import sys
import threading
import time
import tkinter as tk
from tkinter import *
from threading import Thread, Lock

import pyautogui

root = Tk()


class MyThread(threading.Thread):

    # Thread class with a _stop() method.
    # The thread itself has to check
    # regularly for the stopped() condition.

    def __init__(self, *args, **kwargs):
        super(MyThread, self).__init__(*args, **kwargs)
        self._stop = threading.Event()

    # function using _stop function
    def stop(self):
        self._stop.set()



    def stopped(self):
        return self._stop.isSet()



    def run(self):
        CEVA = random.uniform(4, 10)
        time.sleep(CEVA)
        print(CEVA)
        pyautogui.leftClick(815, 330, interval=random.uniform(0.2, 0.9),duration=random.uniform(0.2, 0.9))  # for select all
        pyautogui.leftClick(1225, 800, interval=random.uniform(0.2, 0.9),duration=random.uniform(0.2, 0.9))  # for collect
        print("finish")
        time.sleep(600)
        while True:
            if self.stopped():
                return
            CEVA = random.uniform(0, 300)
            time.sleep(CEVA)
            print(CEVA)
            pyautogui.leftClick(815, 330, interval=random.uniform(0.2, 0.9), duration=random.uniform(0.2, 0.9))  # for select all
            pyautogui.leftClick(1225, 800, interval=random.uniform(0.2, 0.9),duration=random.uniform(0.2, 0.9))  # for collect
            print("finish")
            time.sleep(600)






t1 = MyThread()

canvas = tk.Canvas(root, height=700, width=700, bg="#000000")
canvas.pack()
b = Button(root, text="Start", command=t1.start)
b.pack()
b1 = Button(root, text="quit", command=t1.stop)
b1.pack()


root.mainloop()