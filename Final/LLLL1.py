import importlib
import random
import sys
import threading
import time
import tkinter
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
        self.stop_threads = False

    def ceauceau(self):
        self.stop_threads = True
        time.sleep(1)
        t1.join()

    def run(self):
        CEVA = random.uniform(4, 10)
        time.sleep(CEVA)
        print(CEVA)
        pyautogui.leftClick(random.uniform(813, 818), random.uniform(328, 334), interval=random.uniform(0.2, 0.9),
                            duration=random.uniform(0.2, 0.9))  # for select all
        pyautogui.leftClick(random.uniform(1220, 1260), random.uniform(798, 803), interval=random.uniform(0.2, 0.9),
                            duration=random.uniform(0.2, 0.9))  # for collect
        print("finish")
        time.sleep(2)
        while True:
            global stop_threads
            CEVA = random.uniform(0, 3)
            time.sleep(CEVA)
            print(CEVA)
            pyautogui.leftClick(random.uniform(813, 818), random.uniform(328, 334), interval=random.uniform(0.2, 0.9),
                                duration=random.uniform(0.2, 0.9))  # for select all
            pyautogui.leftClick(random.uniform(1220, 1260), random.uniform(798, 803), interval=random.uniform(0.2, 0.9),
                                duration=random.uniform(0.2, 0.9))  # for collect
            print("finish")
            time.sleep(1)
            print("abcd")
            if self.stop_threads is True:
                print("abcd2")
                break


t1 = MyThread()

canvas = tk.Canvas(root, height=700, width=700, bg="#000000")
canvas.pack()
b = tkinter.Button(root, text="Start", command=threading.Thread(target=t1.run).start)
b.pack()
b2 = tk.Button(root, text="rasamatii", command=threading.Thread(target=t1.ceauceau).start)
b2.pack()
root.mainloop()
