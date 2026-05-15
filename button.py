from tkinter import *
from PIL import Image,ImageTk

count = 0

def click():
    global count
    count += 1
    button1.config(text=" You Clicked")
    print(count)
    
window = Tk()
button1 = Button(window,text="Click Me!",command=click,fg='green',bg='black',activebackground='black',activeforeground='green')
# button2 = Button(window,text="Click Me!",command=click,fg='green',bg='black',activebackground='black',activeforeground='green')
button1.pack()
# button2.pack()

window.mainloop()