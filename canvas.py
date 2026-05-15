# from tkinter import *

# window = Tk()

# canvas = Canvas(window, height=500, width=500)

# canvas.create_line(0,0,500,500,fill='red',width=5)

# points = [250,0,500,500,0,500]
# canvas.create_polygon(points,fill='red',width=3)

# canvas.create_arc(0,0,500,500,fill="red",width=3,style=PIESLICE,start=180)

# canvas.create_arc(2,2,498,498,fill="red",width=3,style=PIESLICE,extent=180)
# canvas.create_arc(2,2,498,498,fill="white",width=3,style=PIESLICE,start=180,extent=180)
# canvas.create_oval(188,188,308,308,fill='white',width=3)

# canvas.pack()
# window.mainloop()

# =========================================================================================

# from tkinter import *

# window = Tk()

# canvas = Canvas(window,height=500,width=500)
# # canvas.create_line(50,50,200,50,width=3,fill='red')
# # canvas.create_rectangle(50,100,300,250,fill='blue',width=3)
# # canvas.create_oval(200,200,400,400,width=3,fill='blue')
# canvas.create_text(200,200,text="Hey This is Nishwa",font=('times new roman',16))

# canvas.pack()
# window.mainloop()

import tkinter as tk

def main():
    root = tk.Tk()
    root.title("My Canvas Drawing")

    # 1. Create the Canvas
    canvas = tk.Canvas(root, width=400, height=300, bg="lightgrey")
    canvas.pack(pady=20)

    # 2. Draw Shapes
    # Line
    canvas.create_line(20, 20, 380, 20, fill="black", width=2)
    
    # Rectangle
    canvas.create_rectangle(50, 50, 150, 150, fill="skyblue", outline="navy", width=2)
    
    # Circle (Oval inside a square)
    canvas.create_oval(200, 50, 300, 150, fill="lightgreen", outline="darkgreen", width=2)
    
    # Triangle (Polygon)
    canvas.create_polygon(350, 50, 380, 150, 320, 150, fill="gold", outline="orange")
    
    # Text
    canvas.create_text(200, 200, text="Tkinter Canvas is Fun!", font=("Helvetica", 14, "bold"), fill="darkred")

    # Run the application
    root.mainloop()

if __name__ == "__main__":
    main()