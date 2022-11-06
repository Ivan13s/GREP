import random
import sys
import threading
import time
import tkinter as tk
from tkinter import *
from threading import Thread, Lock
import pyautogui

stop = threading.Event()


def ceva():
    sys.exit()


def stop():
    stop.set()


def stopped():
    return stop.isSet()


def startbot():
    CEVA = random.uniform(2, 4)
    time.sleep(CEVA)
    print("ceva")
    pyautogui.leftClick(795, 317, interval=random.uniform(0.2, 0.9),duration=random.uniform(0.2, 0.9))  # for select all
    pyautogui.leftClick(1285, 833, interval=random.uniform(0.2, 0.9), duration=random.uniform(0.2, 0.9))  # for collect
    while True:

        print("loop")
        time.sleep(1)
        CEVA1 = random.uniform(0,2)
        time.sleep(CEVA1)
        pyautogui.leftClick(795, 317, interval=random.uniform(0.2, 0.9), duration=random.uniform(0.2, 0.9))
        pyautogui.leftClick(1285, 833, interval=random.uniform(0.2, 0.9), duration=random.uniform(0.2, 0.9))
        if stopped():
            return
        print("Hello, world!")
        time.sleep(1)


t1 = threading.Thread(target=startbot)
t1.start()
time.sleep(1)
t2=threading.Thread(target=stop)
t2.stop()
