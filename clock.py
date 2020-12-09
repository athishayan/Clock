from tkinter import *
from tkinter.ttk import *

from time import strftime

time1 = Tk()
time1.title("Clock")

def time():
    string = strftime('%I:%M:%S %p')
    label.config(text=string)
    label.after(1000, time)

label = Label(time1, font = ("Arial",50), background = "black", foreground = "yellow")
label.pack(anchor='center')

time()

mainloop()