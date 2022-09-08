import ctypes, sys
import tkinter as tk
from tkinter import messagebox

def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

if is_admin():
    print("True")
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
    root.after(1, onTop)

def minimize_check():
    if root.minimize:
        root.deiconify
root.protocol("WM_DELETE_WINDOW", on_closing)
root.attributes('-fullscreen', True)

root.mainloop()
while True:
    onTop()
    minimize_check()

