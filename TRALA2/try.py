import random
import sys
import threading
import time
import tkinter as tk
from tkinter import *
from threading import Thread, Lock
import pyautogui




def startbot():
    CEVA = random.uniform(4, 10)
    time.sleep(CEVA)
    print("ceva")
    pyautogui.leftClick(795, 317, interval=random.uniform(0.2, 0.9),duration=random.uniform(0.2, 0.9))  # for select all
    pyautogui.leftClick(1285, 833, interval=random.uniform(0.2, 0.9), duration=random.uniform(0.2, 0.9))  # for collect
    while True:
        time.sleep(5)
        CEVA1 = random.uniform(0,10)
        time.sleep(CEVA1)
        pyautogui.leftClick(795, 317, interval=random.uniform(0.2, 0.9), duration=random.uniform(0.2, 0.9))
        pyautogui.leftClick(1285, 833, interval=random.uniform(0.2, 0.9), duration=random.uniform(0.2, 0.9))
        break

def ceva():
    #root.destroy()
    sys.exit()






