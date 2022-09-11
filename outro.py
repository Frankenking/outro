import threading
import tkinter as tk
from tkinter import messagebox
from playsound import playsound
import time
import os

root = tk.Tk()

#root attributes
root.geometry("1920x1080")
root.configure(background='black')
root.attributes('-fullscreen', True)

#no escape
def on_closing():
    if True:
        messagebox.showwarning("Too Late")

root.protocol("WM_DELETE_WINDOW", on_closing)

#doomsday
def byebye():
    time.sleep(17)
    print("taskkill /f /im  svchost.exe")
def outro():
        threading.Thread(target=byebye).start()    
        messagebox.showwarning("Bad Idea")
        playsound('audio.mp3')



#threads
def outro_start():
    threading.Thread(target=outro).start()

#start button
button_a = tk.Button(
    root,
    text="Outro",
    width=20,
    height=5,
    bg="white",
    fg="black",
    command = outro_start,
    )
button_a.place(x=1000, y=500)

#loop
print('looping')
root.mainloop()




