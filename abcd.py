import random
import sys
import threading
import time
import tkinter as tk
from tkinter import *
from threading import Thread, Lock
from events import Events
import pyautogui
from pygame import event

root = tk.Tk()
canvas = tk.Canvas(root, width=800, height=800)
canvas.pack()
# #def MOVE():
#     while True:
#         x = random.randint(0, 1920)
#         y = random.randint(0, 1080)
#         pyautogui.moveTo(x, y, duration=4, logScreenshot="parara.jpg")  # for sellect
#         print(x, y)

img = tk.PhotoImage(file="parara.png")
image = canvas.create_image(10, 10, anchor=tk.NW, image=img)


def get(events):
    x = random.randint(0, 800)
    y = random.randint(0, 800)
    canvas.move(image, x.e, y)



root.mainloop()
