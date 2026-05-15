from tkinter import *

def submit():
    input = text.get("1.0",END)
    print(input)
    
window = Tk()

text = Text(window,bg='black',fg='green',font=('arial',20),height=10,width=50,padx=60)
text.pack()
Button(text="Submit",command=submit).pack()

window.mainloop()