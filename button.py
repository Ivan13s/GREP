import threading
from tkinter import Tk


start_btn = Tk.Button(root,Text="Start",command=start_thread
start_btn.pack()
 def start_thread():
    t1= threading.Thread(target=start)
    status=True

def start():
    while status:
        <Main code>


stop_btn = Tk.Button(root,Text="Start",command=start_thread
stop_btn.pack()

def stop():
  status=False