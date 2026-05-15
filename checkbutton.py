# from tkinter import *

# def display():
#     if x.get() == 1:
#         print("Agreed Successfull")
#     else:
#         print("Not Agreed")    

# window = Tk()
# window.config(background='black')
# x = IntVar()
# check = Checkbutton(window, text="I Agree",
#                     command=display,
#                     variable=x,
#                     onvalue=1,
#                     offvalue=0,
#                     fg='green',
#                     bg='black',
#                     activebackground='black',
#                     activeforeground='green')

# check.pack()
# window.mainloop()




from tkinter import *

def change_text():  
    if x.get() == 1:
        check_btn.config(text="Agreed",bg='black',fg='green',activebackground='black',activeforeground='green')    
        label.config(text="Checked",bg='black',fg='green',activebackground='black',activeforeground='green')  
    else:
        check_btn.config(text="Agree")  
        label.config(text="Not Checked")   

window = Tk()
window.config(background='black')
x = IntVar()
check_btn = Checkbutton(text="Agree",command=change_text,onvalue=1,offvalue=0,variable=x,fg='green',bg='black')
check_btn.pack(side="left")
label = Label(window,bg='black')
label.pack(side="right")
window.mainloop()