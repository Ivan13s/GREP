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

    def alive_parada(self):
        self.cultura = True
        print(20 * '-', 'Start festivale', '_' * 20)

    def alive_cleanparada(self):
        self.cultura = False
        print(20 * '-', 'Stop festivale', '_' * 20)

    def FESTIVALE_TEATRE(self):
        time.sleep(15)
        while True:
            if self.cultura:
                while True:
                    time.sleep(1)
                    try:
                        if self.cultura:
                            time.sleep(3)
                            x, y = pyautogui.locateCenterOnScreen("fess.png")
                            print(x, y)
                            r, i = pyautogui.locateCenterOnScreen("ccc.png")
                            print(r, i)
                            time.sleep(1)
                            pyautogui.moveTo(r, i)
                            time.sleep(1)
                            pyautogui.dragTo(80, 400, button='left', duration=0.5)
                            time.sleep(1)
                            sleep(random.uniform(25200,26000))
                            pyautogui.leftClick(x + 85, y - 4)
                            time.sleep(2)
                    except TypeError:
                            time.sleep(0.2)
                            try:
                                time.sleep(0.2)
                                cent = pyautogui.locateCenterOnScreen("cent.png")
                                pyautogui.moveTo(cent)
                                time.sleep(2)
                                cult = pyautogui.locateCenterOnScreen("cult.png")
                                pyautogui.leftClick(cult)
                                time.sleep(1)
                                r, i = pyautogui.locateCenterOnScreen("ccc.png")
                                print(r, i)
                                time.sleep(1)
                                pyautogui.moveTo(r, i)
                                time.sleep(1)
                                pyautogui.dragTo(80, 400, button='left', duration=0.5)
                                time.sleep(1)
                            except TypeError:
                                print("Nu e ok boss.")


    def run(self):
        i = 0
        while True:
            if self.alive:
                for i in range(10):
                    if self.alive:
                        my_progress.step(0.1666666666666667)
                        i += 1
                        print(i)
                        sleep(1)

                    elif self.alive is False:
                        my_progress.stop()
                        my_progress.step(0)
                        break
                    if i == 10 and self.alive is True:
                        print("Good")
                        CEVA = random.uniform(0, 10)
                        print("FARM: ", CEVA)
                        sleep(CEVA)
                        while True:
                            try:
                                if self.alive is True:
                                    time.sleep(1)
                                    k, l = pyautogui.locateCenterOnScreen("sate.png")
                                    print(k, l)
                                    time.sleep(0.1)
                                    pyautogui.leftClick(random.uniform(813, 818), random.uniform(328, 334),
                                                        interval=random.uniform(0.2, 0.9),
                                                        duration=random.uniform(0.2, 0.9))  # for select
                                    pyautogui.leftClick(random.uniform(1220, 1260), random.uniform(798, 803),
                                                        interval=random.uniform(0.2, 0.9),
                                                        duration=random.uniform(0.2, 0.9))  # for collect
                                    my_progress.step(0)
                                break
                            except TypeError:
                                if self.alive is True:
                                    time.sleep(0.1)
                                    print("Inca caut")
                                    time.sleep(0.1)
                                    cent = pyautogui.locateCenterOnScreen("cent.png")
                                    time.sleep(1)
                                    pyautogui.moveTo(cent)
                                    time.sleep(1)
                                    farm = pyautogui.locateCenterOnScreen("farm.png")
                                    time.sleep(1)
                                    pyautogui.leftClick(farm)
                                    time.sleep(1)
                            finally:
                                print("CRATER")


clicker = Clicker()
t3 = Thread(target=clicker.FESTIVALE_TEATRE)
t1 = Thread(target=clicker.run)
t3.start()
t1.start()
s = ttk.Style()
s.theme_use('clam')
s.configure("3.Horizontal.TProgressbar", troughcolor='black', background='red')
my_progress = ttk.Progressbar(root, style='3.Horizontal.TProgressbar',
                              orient=HORIZONTAL, length=100, mode='determinate')
my_progress.pack(padx=10, pady=5)

canvas = tk.Canvas(root, height=400, width=400, bg="#000000")
canvas.pack()

b1 = tkinter.Button(root, text="Start farm", command=clicker.alive_set)
b1.pack()
b2 = tk.Button(root, text="Stop farm", command=clicker.alive_clean)
b2.pack()
b5 = tk.Button(root, text="Start festivale", command=clicker.alive_parada)
b5.pack()
b6 = tk.Button(root, text="Stop festivale", command=clicker.alive_cleanparada)
b6.pack()
label = tk.Label(root, text=f"PARADE DATE:{0} ", fg="dark green",
                 background="black", font="bold", padx=10, pady=10)
label.pack()
root.mainloop()
