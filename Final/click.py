import random
import time
import tkinter
import tkinter as tk
from threading import Thread
# importing libraries
from time import sleep
from tkinter import *
from tkinter import ttk

import pyautogui

root = Tk()


class Clicker:
    def __init__(self):
        self.alive = None
        self.paradis = None
        self.cultura = None

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

    def alive_parada(self):
        self.cultura = True
        print(20 * '-', 'Start festivale+parade+teatre', '_' * 20)

    def alive_cleanparada(self):
        self.cultura = False
        print(20 * '-', 'Stop festivale+parade+teatre', '_' * 20)

    def FESTIVALE_TEATRE(self):
        while True:
            if self.cultura:
                time.sleep(1)
                try:
                    overviews = pyautogui.locateCenterOnScreen("overviews.png")
                    print(overviews)
                    city_festival = pyautogui.locateOnScreen("city_festival.png")
                    print(city_festival)
                except TypeError:
                    print("Nu gasesc overviews")

    def run(self):
        i = 0
        while True:
            if self.alive:
                for i in range(600):
                    if self.alive:
                        my_progress.step(0.1666666666666667)
                        i += 1
                        print(i)
                        sleep(1)

                    elif self.alive is False:
                        my_progress.stop()
                        my_progress.step(0)
                        break
                    if i == 600 and self.alive is True:
                        print("Good")
                        CEVA = random.uniform(0, 300)
                        time.sleep(CEVA)
                        print("FARM: ", CEVA)
                        pyautogui.leftClick(random.uniform(813, 818), random.uniform(328, 334),
                                            interval=random.uniform(0.2, 0.9),
                                            duration=random.uniform(0.2, 0.9))  # for select
                        pyautogui.leftClick(random.uniform(1220, 1260), random.uniform(798, 803),
                                            interval=random.uniform(0.2, 0.9),
                                            duration=random.uniform(0.2, 0.9))  # for collect
                        my_progress.step(0)

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
t3 = Thread(target=clicker.FESTIVALE_TEATRE)
t1.start()
t2.start()
t3.start()
s = ttk.Style()
s.theme_use('clam')
s.configure("3.Horizontal.TProgressbar", troughcolor='black', background='red')
my_progress = ttk.Progressbar(root, style='3.Horizontal.TProgressbar',
                              orient=HORIZONTAL, length=100, mode='determinate')
my_progress.pack(padx=10, pady=5)

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
b5 = tk.Button(root, text="Start festivale+teatre+parade", command=clicker.alive_parada)
b5.pack()
b6 = tk.Button(root, text="Stop festivale+teatre+parade", command=clicker.alive_cleanparada)
b6.pack()
label = tk.Label(root, text=f"PARADE DATE:{0} ", fg="dark green",
                 background="black", font="bold", padx=10, pady=10)
root.mainloop()
