from tkinter import *

def submit():
    res = entry.get()
    print(res)

def delete():
    entry.delete(0,END)
    
def backspace():
    entry.delete(len(entry.get())-1, END)
    
window = Tk()

entry = Entry(window, font=('Arial',20),show="*")
entry.pack(side='left')

submit_button = Button(window, text="SUBMIT", command=submit)
submit_button.pack(side='right')

delete_button = Button(window, text="DELETE", command=delete)
delete_button.pack(side="right")

back_button = Button(window, text="BACKSPACE", command=backspace)
back_button.pack(side="right")

window.mainloop()            

# entry.insert(0,"Any wods")
# entry.config(show="*")
# entry.config(state = DISABLED)