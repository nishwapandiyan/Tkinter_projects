# from tkinter import *

# def drag_start(event):
    
#     widget = event.widget
#     widget.startX = event.x
#     widget.startY = event.y
    
# def drag_Motion(event):
     
#     widget = event.widget
#     x = widget.winfo_x() - widget.startX + event.x
#     y = widget.winfo_y() - widget.startY + event.y
#     widget.place(x=x,y=y)
    
# window = Tk()

# window.geometry("400x400")


# label_1 = Label(height=5,width=10,bg='blue')
# label_1.place(x=50,y=100)

# label = Label(height=5,width=10,bg='red')
# label.place(x=0,y=0)

# label.bind("<Button-1>",drag_start)
# label.bind("<B1-Motion>",drag_Motion)

# label_1.bind("<Button-1>",drag_start)
# label_1.bind("<B1-Motion>",drag_Motion)

# window.mainloop()

# ==================================================================================


from tkinter import *

def makedrag(box):
    
    box.bind('<Button-1>',drag_start)
    box.bind('<B1-Motion>',dragMotion)
    
def drag_start(event):
    widget = event.widget
    widget.startX = event.x
    widget.startY = event.y
    widget.lift()

def dragMotion(event):
    widget = event.widget
    x = widget.winfo_x() - widget.startX + event.x
    y = widget.winfo_y() - widget.startY + event.y
    widget.place(x=x,y=y)
    
window = Tk()

Box1 = Label(window,text="Box-1",height=5,width=10,bg='red',fg='white')
Box1.pack()

Box2 = Label(window,text="Box-2",height=5,width=10,bg='green',fg='white')
Box2.pack()

Box3 = Label(window,text="Box-3",height=5,width=10,bg='violet',fg='white')
Box3.pack()

for box in(Box1,Box2,Box3):
    makedrag(box)
    
window.mainloop()