# from tkinter import *
# from tkinter import filedialog

# def select():
#     filepath = filedialog.askopenfilenames(
#         title="select file",
#         filetypes=[
#             ("text files", "*.txt"),
#             ("python files","*.py"),
#             ("all files", "*.*")
#         ])
        
#     if filepath:
#         print("File Selected")
#     else:
#         print("Not selected")        
        
#     for name in filepath:
#         print(name)    
# window = Tk()

# Button(text="Click" ,command=select).pack()
# window.mainloop()


#===============================================================


from tkinter import *
from tkinter import filedialog


# def saveFile():
#     filepath = filedialog.asksaveasfile(defaultextension=".txt",filetypes=[("text file","*.txt"),("python files","*.py"),("all files","*.*")])
#     write = str(text.get(1.0, END))
#     filepath.write(write)
#     filepath.close()
# Window = Tk()

# Button(text="Save", command=saveFile).pack()
# text = Text(Window)
# text.pack()
# Window.mainloop()

def openFile():
    
    filepath = filedialog.askopenfile(mode='r')
    print(filepath.read())
    filepath.close()
window = Tk()

Button(text="open", command=openFile).pack()
window.mainloop()