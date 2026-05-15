from tkinter import *

def NewOpen():
    # new = Toplevel()
    new_dis = Tk()
    label = Label(new_dis,text="This is New Window")
    label.pack()

window = Tk()

Button(window,text="Open New",command=NewOpen).pack()

window.mainloop()