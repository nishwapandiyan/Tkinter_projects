from tkinter import *

window = Tk()

window.title("Grid Geometry")
window.geometry("500x500")

Label(window,text="Username:",bg='blue').grid(row=0,column=0,padx=10,pady=10,sticky='w')
Entry(window).grid(row=0,column=1,padx=10,pady=10)

Label(window,text="Gmail:",bg='red').grid(row=1,column=0  ,padx=10,pady=10,sticky='w')
Entry(window).grid(row=0,column=1,padx=10,pady=10)

Label(window,text="Password:",bg='yellow').grid(row=2,column=0,padx=10, pady=10,sticky='w')
Entry(window,show="*").grid(row=1,column=1,padx=10,pady=10)

Button(window,text="Submit").grid(row=2,column=0,columnspan=2)

window.mainloop()

