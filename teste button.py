
import random
import time
from tkinter import *
import pyautogui

running = False  # Global flag
idx = 0  # loop index

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

while True:
    if idx % 500 == 0:
        root.update()

    if running:
        CEVA = random.uniform(4, 10)
        time.sleep(CEVA)
        print(CEVA)
        pyautogui.leftClick(random.uniform(813, 818), random.uniform(328, 334), interval=random.uniform(0.2, 0.9),duration=random.uniform(0.2, 0.9))  # for select all
        pyautogui.leftClick(random.uniform(1220, 1260), random.uniform(798, 803), interval=random.uniform(0.2, 0.9),duration=random.uniform(0.2, 0.9))  # for collect

        while True:
            time.sleep(600)
            CEVA = random.uniform(0, 300)
            time.sleep(CEVA)
            print(CEVA)
            pyautogui.leftClick(random.uniform(813, 818), random.uniform(328, 334), interval=random.uniform(0.2, 0.9),duration=random.uniform(0.2, 0.9))  # for select all
            pyautogui.leftClick(random.uniform(1220, 1260), random.uniform(798, 803), interval=random.uniform(0.2, 0.9),duration=random.uniform(0.2, 0.9))  # for collect

        print("hello")
        idx += 1