import importlib
import os
import random
import sys
import textwrap
import threading
import time
import tkinter
import tkinter as tk
from tkinter import *
from threading import Thread, Event
from tkinter import ttk
from tkinter.messagebox import showinfo
# importing libraries
from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sys
import pandas as pd
import numpy as np
from time import sleep
from termcolor import colored
from tqdm import tqdm, trange
import pyautogui

root = Tk()


class Clicker:
    def __init__(self):
        super().__init__()
        self.alive = None
        self.paradis = None
        super().__init__()

        # setting title
        #self.setWindowTitle("Python ")

        # setting geometry
        #self.setGeometry(100, 100, 600, 400)

        # calling method
        self.UiComponents()

        # showing all the widgets
        #self.show()


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

    def UiComponents(self):

        # creating progress bar
        bar = QProgressBar()

        # setting geometry to progress bar
        bar.setGeometry(200, 150, 200, 30)

        # set value to progress bar
        bar.setValue(70)

        # setting text
        bar.setFormat('This is progress bar')

        # setting alignment to centre
        bar.setAlignment(Qt.AlignCenter)


    def run(self):
        i = 0
        while True:
            if self.alive:
                for i in range(10):
                    if self.alive:
                        # my_progress.step(10)
                        i += 1
                        print(i)
                        sleep(1)

                    elif self.alive is False:
                        # my_progress.stop()
                        # my_progress.step(0)
                        break
                    if i == 10 and self.alive is True:
                        print("Good")
                        # my_progress.stop()
                        clicker.UiComponents()
                        CEVA = random.uniform(3, 6)
                        time.sleep(CEVA)

                        print("FARM: ", CEVA)
                        pyautogui.leftClick(random.uniform(813, 818), random.uniform(328, 334),
                                            interval=random.uniform(0.2, 0.9),
                                            duration=random.uniform(0.2, 0.9))  # for select
                        pyautogui.leftClick(random.uniform(1220, 1260), random.uniform(798, 803),
                                            interval=random.uniform(0.2, 0.9),
                                            duration=random.uniform(0.2, 0.9))  # for collect


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
                    pyautogui.leftClick(x, y+30, duration=random.uniform(0, 2))
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
# s = ttk.Style()
# s.theme_use('clam')
# s.configure("3.Horizontal.TProgressbar", troughcolor ='black', background='red')
# my_progress = ttk.Progressbar(root, style='3.Horizontal.TProgressbar', orient=HORIZONTAL, length=100,
#                               mode='determinate',)
printProgressBar()

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
label = tk.Label(root, text=f"PARADE DATE:{0} ", fg="dark green", background="black", font="bold", padx=10, pady=10)
label.pack()
root.mainloop()
