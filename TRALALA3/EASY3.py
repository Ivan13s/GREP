import random
import sys
import threading
import time
import tkinter as tk
from tkinter import *
from threading import Thread, Lock
import pyautogui

root = Tk()


def startbot():
    CEVA = random.uniform(4, 10)
    time.sleep(CEVA)
    pyautogui.leftClick(795, 317, interval=random.uniform(0.2, 0.9),duration=random.uniform(0.2, 0.9))  # for select all
    pyautogui.leftClick(1285, 833, interval=random.uniform(0.2, 0.9), duration=random.uniform(0.2, 0.9))  # for collect
    while True:
        time.sleep(600)
        CEVA1 = random.uniform(0,300)
        time.sleep(CEVA1)
        pyautogui.leftClick(795, 317, interval=random.uniform(0.2, 0.9), duration=random.uniform(0.2, 0.9))
        pyautogui.leftClick(1285, 833, interval=random.uniform(0.2, 0.9), duration=random.uniform(0.2, 0.9))


def ceva():
    root.destroy()
    sys.exit()
def stop():
    stop.set()

def stopped(self):
    return stop.isSet()


canvas = tk.Canvas(root, height=700, width=700, bg="#000000")
canvas.pack()
b = Button(root, text="Start", command=threading.Thread(target=startbot, daemon=True).start)
b.pack()
b1 = Button(root, text="quit", command=threading.Thread(target=ceva, daemon=True).start)
b1.pack()


root.mainloop()
