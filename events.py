# from tkinter import *

# def doSomething(event):
#     # print("You Pressed:"+ event.keysym)
#     x.set(event.keysym)
    
# window = Tk()

# x = StringVar()

# window.bind("<Key>",doSomething)
# label = Label(window,textvariable=x,font=('consolas',20))
# label.pack()

# window.mainloop()

# ==================================================================================================

from tkinter import *

def doSomething(event):
    
    print(str(event.x)+" "+str(event.y))
    
window = Tk()

# window.bind("<Button-1>",doSomething)
# window.bind("<Button-2>",doSomething)
# window.bind("<Button-3>",doSomething)
# window.bind("<ButtonRelease>",doSomething)
# window.bind("<Enter>",doSomething)
# window.bind("<Leave>",doSomething)
# window.bind("<Motion>",doSomething)

window.mainloop()