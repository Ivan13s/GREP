from tkinter import Button, Frame, Tk

import random
import sys
import threading
import time
import tkinter as tk
from tkinter import *
from threading import Thread, Lock
import pyautogui

running = True  # Global flag

def scanning():
    if running:  # Only do this if the Stop button has not been clicked
        print("hello")

    # After 1 second, call scanning again (create a recursive loop)
#

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

start = Button(app, text="Start Scan", command=scanning)
stop = Button(app, text="Stop", command=stop)

start.grid()
stop.grid()
  # After 1 second, call scanning
root.mainloop()