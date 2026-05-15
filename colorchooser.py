from tkinter import *
from tkinter import colorchooser

def color():
    color = colorchooser.askcolor()
    window.config(bg=color[1])
window = Tk()

window.geometry("400x400")
Button(text="Click",command=color).pack()
window.mainloop()