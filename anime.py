# from tkinter import *
# import time

# window = Tk()

# WIDTH = 500
# HEIGHT = 500

# xVelocity = 1
# yVelocity = 2

# canvas = Canvas(window,width=WIDTH,height=HEIGHT)
# canvas.pack()

# img = PhotoImage(file='car.png')
# res = img.subsample(9,9)

# my_image = canvas.create_image(0,0,image=res,anchor=NW)

# image_width = res.width()
# image_height = res.height()

# while True:
#     coordinates = canvas.coords(my_image)
#     if coordinates[0] > WIDTH-image_width or coordinates[0] < 0:
#         xVelocity = -xVelocity
        
#     if coordinates[1] > HEIGHT-image_height or coordinates[1] < 0:
#         yVelocity = -yVelocity 
               
#     canvas.move(my_image,xVelocity,yVelocity)
#     window.update()
#     time.sleep(0.01)
    
# window.mainloop()

# =====================================================

# def animate():
    
#     cur_x = label.winfo_x()
#     if cur_x<300:
#         label.place(x=cur_x+5, y=100)
#         window.ater(20,animate)
# from tkinter import *

# window = Tk()

# label = Label(window,bg='red',width=5,height=2)
# label.place(x=0,y=0)

# Button(text="Start", command=animate).place(x=10,y=10)
# window.mainloop()

#================================================================================

from tkinter import *
from Ball import *
import time

window = Tk()


WIDTH = 500
HEIGHT = 500

canvas = Canvas(window,height=HEIGHT,width=WIDTH)
canvas.pack()

volleyball = Ball(canvas,0,0,100,1,3,"yellow")
tennis = Ball(canvas,0,0,30,2,4,"green")
cricket = Ball(canvas,0,0,40,2,2,"red")
golf = Ball(canvas,0,0,20,2,3,"white")
while True:
    volleyball.move()
    tennis.move()
    cricket.move()
    golf.move()
    window.update()
    time.sleep(0.01)
    

window.mainloop()