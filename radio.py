# from tkinter import *
# choice = ["Pizza","Burger","Chocolate"]

# def dis():
#     if (x.get() == 0):
#         label.config(text="You ordered Pizza")
#     elif (x.get() == 1):
#         label.config(text="You ordered Burger")
#     elif (x.get() == 2):
#         label.config(text="You ordered Chocolate")        
#     else:
#         label.config(text="Huh??")    
# window = Tk()

# x = IntVar()
# for i in range(len(choice)):
#     radio = Radiobutton(window,text=choice[i],value=i,variable=x,command=dis)
#     radio.pack(anchor= W)
    
# label = Label(window)
# label.pack()    
    
# window.mainloop()

# ======================================================================================================================================
from tkinter import *

def show():
    label.config(text=var.get())

root = Tk()

var = StringVar()

Radiobutton(root, text="Python", variable=var, value="Python").pack()

Radiobutton(root, text="Java", variable=var, value="Java").pack()

Button(root, text="Submit", command=show).pack()

label = Label(root)
label.pack()

root.mainloop()
