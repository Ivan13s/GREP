import random
import time
import tkinter
import tkinter as tk
from faulthandler import disable
from threading import Thread
# importing libraries
from time import sleep
from timeit import timeit
from tkinter import *
from tkinter import ttk

import pyautogui

root = Tk()
class Clicker:
    def __init__(self):
        self.alive = None


    def alive_set(self):
        self.alive = True
        print(20 * '-', 'Start farm', '_' * 20)

    def alive_clean(self):
        self.alive = False
        print(20 * '-', 'Stop farm', '_' * 20)

    def run(self):

clicker = Clicker()
t1 = Thread(target=clicker.run)