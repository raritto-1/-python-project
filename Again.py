import pyautogui
from tkinter import PhotoImage
import tkinter as tk 
import time

def take_screenshot(event =None):
    win.update()
    time.sleep(4)
    ss = pyautogui.screenshot()
    ss.save("screenshot.png")

def on_enter(event):
    button.config(bg="lightblue")

def on_leave(event):
    button.config(bg="SystemButtonFace")


win = tk.Tk()
win.title ("its screenshort time")
win.geometry()



file_path =  r"D:\vs code\python-sheet\image.png"
bg = PhotoImage(file = file_path) 



label = tk.Label(win, image=bg)
label.place(x=0, y=0, relwidth=1, relheight=1)

button_img = PhotoImage(file="button_image.png")
button = tk.Button(win, image=button_img, command=take_screenshot)
button.pack(expand=True)


button.bind("<Enter>", on_enter)
button.bind("<Leave>", on_leave)
button.bind("<Button-1>", take_screenshot)

win.mainloop()