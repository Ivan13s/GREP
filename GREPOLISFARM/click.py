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
from termcolor import colored
import pyautogui

root = Tk()


class Clicker:
    def __init__(self):
        self.alive = None
        self.paradis = None

    def alive_set(self):
        self.alive = True
        print(20 * '-', 'Started', '_' * 20)

    def alive_clean(self):
        self.alive = False
        print(20 * '-', 'Stopped', '_' * 20)

    def alive_parade(self):
        self.paradis = True
        print(20 * '-', 'Started parada cu orfeu', '_' * 20)

    def alive_cleanparade(self):
        self.paradis = False
        print(20 * '-', 'Stopped parada cu orfeu', '_' * 20)

    def run(self):
        while True:
            if self.alive:
                time.sleep(1)
                CEVA = random.uniform(0, 2)
                time.sleep(CEVA)
                print("FARM: ", CEVA)
                pyautogui.leftClick(random.uniform(813, 818), random.uniform(328, 334),interval=random.uniform(0.2, 0.9),duration=random.uniform(0.2, 0.9))  # for selel
                pyautogui.leftClick(random.uniform(1220, 1260), random.uniform(798, 803),interval=random.uniform(0.2, 0.9), duration=random.uniform(0.2, 0.9))  # for collect

    def parade(self):
        count = 0
        while True:
            if self.paradis:
                time.sleep(1)
                try:
                    x, y = pyautogui.locateCenterOnScreen("paradaorfeu.png")
                    generate=random.uniform(0,5)
                    time.sleep(generate)
                    print(generate)
                    pyautogui.leftClick(x, y + 30, duration=random.uniform(0, 2))
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

canvas = tk.Canvas(root, height=700, width=700, bg="#000000")
canvas.pack()

b1 = tkinter.Button(root, text="Start", command=clicker.alive_set)
b1.pack()
b2 = tk.Button(root, text="Stopped", command=clicker.alive_clean)
b2.pack()
b3 = tkinter.Button(root, text="Start parada cu orfeul", command=clicker.alive_parade)
b3.pack()
b4 = tk.Button(root, text="Stop parada cu orfeu", command=clicker.alive_cleanparade)
b4.pack()
label=tk.Label(root,text="PARADE DATE: ",fg="dark green",background="black",font="bold")
label.pack()
root.mainloop()
