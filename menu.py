from tkinter import *
from tkinter import filedialog

def NewFile():
    text.pack()
    text.delete(1.0, END)

def OpenFile():
    filepath = filedialog.askopenfile(mode='r')
    if filepath is not None:
        text.pack()
        text.delete(1.0, END)
        text.insert(1.0, filepath.read())
        filepath.close()
    

def SaveFile():
    filepath = filedialog.asksaveasfile(defaultextension='.txt')
    
    if filepath is not None:
            file = text.get(1.0,END)
            filepath.write(file)
            filepath.close()


window = Tk()

menubar = Menu(window)
window.config(menu=menubar)

text = Text(window)

FileMenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="File", menu=FileMenu)

FileMenu.add_command(label="New",command=NewFile)
FileMenu.add_command(label="Open",command=OpenFile)
FileMenu.add_command(label="Save",command=SaveFile)
FileMenu.add_separator()
FileMenu.add_command(label="Exit",command=window.destroy)


window.mainloop()


# from tkinter import *
# from tkinter import filedialog

# def NewFile():
#     text_area.pack(expand=True, fill='both')
#     text_area.delete(1.0, END)

# def OpenFile():
#     filepath = filedialog.askopenfile(mode='r')
    
#     if filepath is not None:
#         text_area.pack(expand=True, fill='both')
#         text_area.delete(1.0, END)
#         text_area.insert(1.0, filepath.read())
#         filepath.close()

# def SaveFile():
#     filepath = filedialog.asksaveasfile(defaultextension='.txt')
#     if filepath is not None:
#         file_content = text_area.get(1.0, END)
#         filepath.write(file_content)
#         filepath.close()

# window = Tk()
# window.title("My Python Notepad")
# window.geometry("400x300") 

# text_area = Text(window)

# menubar = Menu(window)
# window.config(menu=menubar)

# FileMenu = Menu(menubar, tearoff=0)
# menubar.add_cascade(label="File", menu=FileMenu)

# FileMenu.add_command(label="New", command=NewFile)
# FileMenu.add_command(label="Open", command=OpenFile)
# FileMenu.add_command(label="Save", command=SaveFile)
# FileMenu.add_separator()
# FileMenu.add_command(label="Exit", command=window.destroy)

# window.mainloop()