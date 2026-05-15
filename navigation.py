# from tkinter import *
# from PIL import Image, ImageTk

# def moveUp(event):
#     label.place(x = label.winfo_x() ,y = label.winfo_y() - 30)
    
# def moveDown(event):
#     label.place(x = label.winfo_x() ,y = label.winfo_y() + 30)
    
# def moveLeft(event):
#     label.place(x = label.winfo_x() - 30 ,y = label.winfo_y())
    
# def moveRight(event):
#     label.place(x = label.winfo_x() + 30 ,y = label.winfo_y())            

# window = Tk()
# window.geometry("700x300")

# # img = Image.open("car.png")
# # img_tk = ImageTk.PhotoImage(img)
# # res = img_tk.resize((200,200),Image.Resampling.LANCZOS)
# # Label(window,image=res).pack()

# icon = PhotoImage(file="car.png")
# res_icon = icon.subsample(9,9)
# label = Label(window,image=res_icon)
# label.place(x=0,y=0)

# window.bind('<w>',moveUp)
# window.bind('<s>',moveDown)
# window.bind('<a>',moveLeft)
# window.bind('<d>',moveRight)

# window.bind('<Up>',moveUp)
# window.bind('<Down>',moveDown)
# window.bind('<Left>',moveLeft)
# window.bind('<Right>',moveRight)

# window.mainloop()

# ====================================================== WITH CANVAS ========================================= #

from tkinter import *


def moveUp(event):
    canvas.move(image,0,-10)
    
def moveDown(event):
    canvas.move(image,0,10)
    
def moveLeft(event):
    canvas.move(image,-10,0)
    
def moveRight(event):
    canvas.move(image,10,0)    

window = Tk()

canvas = Canvas(window,height=500,width=500)

icon = PhotoImage(file='car.png')
img = icon.subsample(9,9)
image = canvas.create_image(0,0,image=img,anchor=NW)

window.bind('<w>',moveUp)
window.bind('<s>',moveDown)
window.bind('<a>',moveLeft)
window.bind('<d>',moveRight)

window.bind('<Up>',moveUp)
window.bind('<Down>',moveDown)
window.bind('<Left>',moveLeft)
window.bind('<Right>',moveRight)

canvas.pack()

window.mainloop()