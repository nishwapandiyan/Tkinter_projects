# from tkinter import *


# def submit():
#     print("Ordered:"+list.get(list.curselection()))
    
# def add():
#     list.insert(list.size(),entry.get())
#     list.config(height=list.size())
    
# def delete():
#     list.delete(list.curselection())
#     list.config(height=list.size())

# window = Tk()

# list = Listbox(window,bg='black',fg='green',font=('arial',20),width=15)
# list.pack()
# list.insert(0,"Pizza")
# list.insert(1,"Burger")
# list.insert(2,"Coc")

# list.config(height=list.size())

# entry = Entry(window,font=('arial',20),bg='blue',fg='orange')
# entry.pack()
# Button(text='Submit',command=submit).pack()
# Button(text='Add',command=add).pack()
# Button(text='Delete',command=delete).pack()
# window.mainloop()


# ================================================= SINGLE SELECTION ==========================================================
# def select():
#     print(str(list.get(list.curselection()))+" Ordered")
    
# def delete():
#     list.delete(list.curselection())    
#     list.config(height=list.size())
    
# def add():
#     list.insert(END,entry.get())   
#     list.config(height=list.size()) 
    
# from tkinter import *

# window = Tk()
# list = Listbox(window,font=('arial',20),width=15,bg='black',fg='green')
# list.pack()
# foods = ["Pizza","Burger","Soda","Cola"]

# for food in foods:
#     list.insert(END,food)
#     list.config(height=list.size())

# entry = Entry(window,bg='black',fg='green',font=('arial',20))
# entry.pack()
# Button(text="Add",command=add).pack()
# Button(text="Select",command=select).pack()    
# Button(text="Delete",command=delete).pack()

# window.mainloop()

# ============================================================= MULTIPLE SELECTION ==================================================

def select():
    print("you ordered:")
    for i in list.curselection():
        print(list.get(i))
    
def delete():
    for i in reversed(list.curselection()):
        list.delete(i)
        list.config(height=list.size())
    
def add():
    list.insert(END,entry.get())   
    entry.delete(0,END)
    list.config(height=list.size()) 
    
from tkinter import *

window = Tk()
list = Listbox(window,font=('arial',20),width=15,bg='black',fg='green',selectmode="multiple")
list.pack()
foods = ["Pizza","Burger","Soda","Cola"]

for food in foods:
    list.insert(END,food)
    list.config(height=list.size())

entry = Entry(window,bg='black',fg='green',font=('arial',20))
entry.pack()
Button(text="Add",command=add).pack()
Button(text="Select",command=select).pack()    
Button(text="Delete",command=delete).pack()

window.mainloop()