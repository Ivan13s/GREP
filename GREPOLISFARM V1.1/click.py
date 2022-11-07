import importlib
import os
import random
import sys
import threading
import time
import tkinter
import tkinter as tk
from tkinter import *
from threading import Thread, Event
from tkinter import ttk
import pandas as pd
import numpy as np
from time import sleep
from termcolor import colored
from tqdm import tqdm, trange
import pyautogui

root = Tk()


class Clicker:
    def __init__(self):
        self.alive = None
        self.paradis = None

    def alive_set(self):
        self.alive = True
        print(20 * '-', 'Start farm', '_' * 20)

    def alive_clean(self):
        self.alive = False
        print(20 * '-', 'Stop farm', '_' * 20)

    def alive_parade(self):
        self.paradis = True
        print(20 * '-', 'Started parada cu orfeu', '_' * 20)

    def alive_cleanparade(self):
        self.paradis = False
        print(20 * '-', 'Stopped parada cu orfeu', '_' * 20)

    def run(self):
        i = 0
        while True:
            if self.alive:
                for i in range(600):
                    if self.alive:
                        my_progress.start(interval=6000)
                        i += 1
                        print(i)
                        sleep(1)
                    if self.alive is False or i == 600:
                        my_progress.stop()

                print("Good")
                CEVA = random.uniform(2, 5)
                time.sleep(CEVA)
                print("FARM: ", CEVA)
                pyautogui.leftClick(random.uniform(813, 818), random.uniform(328, 334),
                                    interval=random.uniform(0.2, 0.9), duration=random.uniform(0.2, 0.9))  # for selel
                pyautogui.leftClick(random.uniform(1220, 1260), random.uniform(798, 803),
                                    interval=random.uniform(0.2, 0.9), duration=random.uniform(0.2, 0.9))  # for collect

    def parade(self):
        count = 0
        while True:
            if self.paradis:
                time.sleep(1)
                try:
                    x, y = pyautogui.locateCenterOnScreen("paradaorfeu.png")
                    generate = random.uniform(0, 5)
                    time.sleep(generate)
                    print(generate)
                    pyautogui.leftClick(x, y, duration=random.uniform(0, 2))
                    count += 1
                    print("Parade date: ", count)
                    label.config(text=f"PARADE DATE:{str(count)}")
                except TypeError:
                    time.sleep(1)
                    print("Inca n-am gasit nimica")


clicker = Clicker()
t1 = Thread(target=clicker.run)
t2 = Thread(target=clicker.parade)
t1.start()
t2.start()
my_progress = ttk.Progressbar(root, orient=HORIZONTAL, length=600, mode='determinate')
my_progress.pack()
canvas = tk.Canvas(root, height=700, width=700, bg="#000000")
canvas.pack()

b1 = tkinter.Button(root, text="Start farm", command=clicker.alive_set)
b1.pack()
b2 = tk.Button(root, text="Stop farm", command=clicker.alive_clean)
b2.pack()
b3 = tkinter.Button(root, text="Start parada cu orfeul", command=clicker.alive_parade)
b3.pack()
b4 = tk.Button(root, text="Stop parada cu orfeu", command=clicker.alive_cleanparade)
b4.pack()
label = tk.Label(root, text="PARADE DATE: ", fg="dark green", background="black", font="bold", padx=10, pady=10)
label.pack()
root.mainloop()
