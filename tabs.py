from tkinter import *
from tkinter import ttk

window = Tk()
notebook = ttk.Notebook(window)

tab1 = Frame(notebook,bg="blue")
tab2 = Frame(notebook,bg="red")

notebook.add(tab1,text="Tab-1")
notebook.add(tab2,text="Tab-2")
notebook.pack(expand=True, fill="both")

Label(tab1,text="This is tab 1").pack()
Label(tab2,text="This is tab 2").pack()

window.mainloop()