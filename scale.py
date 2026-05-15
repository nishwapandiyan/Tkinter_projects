from tkinter import *

def submit():
    print("The Value is:"+str(scale.get()))
window = Tk()

scale = Scale(from_=100,to=0,length=600,resolution=5,tickinterval=10,troughcolor='blue',bg='black',fg='orange')
scale.pack()
Button(text="Submit",command=submit).pack()

window.mainloop()