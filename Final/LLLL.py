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

    def stop(self):
        global game_alive
        game_alive = False

    def run(self):
        global game_alive
        CEVA = random.uniform(4, 10)
        time.sleep(CEVA)
        print(CEVA)
        pyautogui.leftClick(random.uniform(813, 818), random.uniform(328, 334), interval=random.uniform(0.2, 0.9),
                            duration=random.uniform(0.2, 0.9))  # for select all
        pyautogui.leftClick(random.uniform(1220, 1260), random.uniform(798, 803), interval=random.uniform(0.2, 0.9),
                            duration=random.uniform(0.2, 0.9))  # for collect

        while game_alive:
            time.sleep(600)
            CEVA = random.uniform(0, 300)
            time.sleep(CEVA)
            print(CEVA)
            pyautogui.leftClick(random.uniform(813, 818), random.uniform(328, 334), interval=random.uniform(0.2, 0.9),
                                duration=random.uniform(0.2, 0.9))  # for select all
            pyautogui.leftClick(random.uniform(1220, 1260), random.uniform(798, 803), interval=random.uniform(0.2, 0.9),
                                duration=random.uniform(0.2, 0.9))  # for collect


t1 = MyThread()

canvas = tk.Canvas(root, height=700, width=700, bg="#000000")
canvas.pack()
game_alive = True
b = tkinter.Button(root, text="Start", command=threading.Thread(target=t1.run).start)
b.pack()
b2 = tk.Button(root, text="rasamatii", command=threading.Thread(target=t1.stop).start)
b2.pack()
root.mainloop()
