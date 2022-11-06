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
from multiprocessing import Process,Pool


root=tkinter.Tk()

def task():
    time.sleep(1)
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





papuci = True
def prostie():
    papuci=False
    print("Prostie")
    return papuci
def start():
    papuci=True
    print("Start")
    return papuci

def Ceva():
    time.sleep(1)
    print("Start Ceva")
    while papuci is True:
        thread1 = Thread(target=task)
        thread1.start()
        thread1.join()
        if prostie() is True:
            return


canvas = tk.Canvas(root, height=700, width=700, bg="#000000")
canvas.pack()

t1=threading.Thread(name="Start",target=start)
t2=threading.Thread(name="Prostie",target=prostie)
t3=threading.Thread(name="Ceva",target=Ceva)

b1= Button(root, text="Start", command=t1.start)
b1.pack()
b2 = Button(root, text="Prostie", command=t2.start)
b2.pack()
b3 = Button(root, text="Ceva", command=t3.start)
b3.pack()
root.mainloop()