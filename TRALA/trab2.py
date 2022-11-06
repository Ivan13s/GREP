import threading
import time

# This function gets called by our thread.. so it basically becomes the thread init...
import random
import tkinter
import pyautogui
import importlib
import random
import sys
import threading
import time
import tkinter as tk
from tkinter import *
from threading import Thread, Lock

root = Tk()

import pyautogui

def wait_for_event(e,):
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
        CEVA = random.uniform(0, 3)
        time.sleep(CEVA)
        print(CEVA)
        pyautogui.leftClick(random.uniform(813, 818), random.uniform(328, 334), interval=random.uniform(0.2, 0.9),duration=random.uniform(0.2, 0.9))  # for select all
        pyautogui.leftClick(random.uniform(1220, 1260), random.uniform(798, 803), interval=random.uniform(0.2, 0.9), duration=random.uniform(0.2, 0.9))  # for collect
        print("finish")
        time.sleep(1)
        print("abcd")

# Main code
e = threading.Event()
canvas = tk.Canvas(root, height=700, width=700, bg="#000000")
canvas.pack()
t = threading.Thread(name='pausable_thread', target=wait_for_event, args=(e,))
t2 = threading.Thread(name='pausable_thread', target=wait_for_event,args=(e,),daemon=True)
b = Button(root, text="Start", command=t.start)
b.pack()
b2 = Button(root, text="rasamatii", command=t2.start)
b2.pack()
root.mainloop()
