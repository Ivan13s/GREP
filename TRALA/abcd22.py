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
        self._stop1 = threading.Event()

    # function using _stop function
    def stop(self):
        self._stop1.set()
        time.sleep(1)
        self._stop1.wait()



    def run(self):
        CEVA = random.uniform(4, 10)
        time.sleep(CEVA)
        print(CEVA)
        pyautogui.leftClick(815, 330, interval=random.uniform(0.2, 0.9),duration=random.uniform(0.2, 0.9))  # for select all
        pyautogui.leftClick(1225, 800, interval=random.uniform(0.2, 0.9),duration=random.uniform(0.2, 0.9))  # for collect
        print("finish")
        time.sleep(2)
        while True:
            CEVA = random.uniform(0, 2)
            time.sleep(CEVA)
            print(CEVA)
            pyautogui.leftClick(815, 330, interval=random.uniform(0.2, 0.9), duration=random.uniform(0.2, 0.9))  # for select all
            pyautogui.leftClick(1225, 800, interval=random.uniform(0.2, 0.9),duration=random.uniform(0.2, 0.9))  # for collect
            print("finish")
            time.sleep(1)
            self._stop1.clear()



t1 = MyThread()

canvas = tk.Canvas(root, height=700, width=700, bg="#000000")
canvas.pack()
b = Button(root, text="Start", command=threading.Thread(target=t1.run).start)
b.pack()
b1 = Button(root, text="quit", command=threading.Thread(target=t1.stop,args=(self._stop1,)).start)
b1.pack()


root.mainloop()
