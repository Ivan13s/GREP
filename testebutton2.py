import time
from random import random
from tkinter import Tk
from tkinter.ttk import Button, Frame
import random

import pyautogui

running = False  # Global flag

def scanning():
    if running:  # Only do this if the Stop button has not been clicked
        CEVA = random.uniform(4, 10)
        time.sleep(CEVA)
        print(CEVA)
        pyautogui.leftClick(random.uniform(813, 818), random.uniform(328, 334), interval=random.uniform(0.2, 0.9),duration=random.uniform(0.2, 0.9))  # for select all
        pyautogui.leftClick(random.uniform(1220, 1260), random.uniform(798, 803), interval=random.uniform(0.2, 0.9),duration=random.uniform(0.2, 0.9))
        while True:
            time.sleep(600)
            CEVA = random.uniform(0, 300)
            time.sleep(CEVA)
            print(CEVA)
            pyautogui.leftClick(random.uniform(813, 818), random.uniform(328, 334), interval=random.uniform(0.2, 0.9),duration=random.uniform(0.2, 0.9))  # for select all
            pyautogui.leftClick(random.uniform(1220, 1260), random.uniform(798, 803), interval=random.uniform(0.2, 0.9),duration=random.uniform(0.2, 0.9))  # for collect
    # After 1 second, call scanning again (create a recursive loop)
    root.after(1000, scanning)

def start():
    """Enable scanning by setting the global flag to True."""
    global running
    running = True

def stop():
    """Stop scanning by setting the global flag to False."""
    global running
    running = False

root = Tk()
root.title("Title")
root.geometry("500x500")

app = Frame(root)
app.grid()

start = Button(app, text="Start Scan", command=start)
stop = Button(app, text="Stop", command=stop)

start.grid()
stop.grid()

root.after(1000, scanning)  # After 1 second, call scanning
root.mainloop()