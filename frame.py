# from tkinter import *

# window = Tk()

# frame = Frame(window,bg='red',relief='raised',bd=15)
# frame.pack()

# Button(frame, text='W').pack(side='top')
# Button(frame, text='A').pack(side='left')
# Button(frame, text='S').pack(side='left')
# Button(frame, text='D').pack(side='left')

# window.mainloop()


# ======================================================================================================================================= #

import tkinter as tk


root = tk.Tk()

root.title("Tkinter Frames Example")
root.geometry("300x200")


top_frame = tk.Frame(root, bg="lightblue", bd=2, relief="groove", padx=10, pady=10)
bottom_frame = tk.Frame(root, bg="lightgrey", bd=2, relief="sunken", padx=10, pady=10)


top_frame.pack(side="top", fill="x", pady=5)
bottom_frame.pack(side="bottom", fill="both", expand=True, pady=5)

btn1 = tk.Button(top_frame, text="Button 1")
btn1.pack(side="left", padx=5)

btn2 = tk.Button(top_frame, text="Button 2")
btn2.pack(side="left", padx=5)


label = tk.Label(bottom_frame, text="This label is in the bottom frame.")
label.pack()

root.mainloop()