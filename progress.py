# from tkinter import *
# from tkinter.ttk import *
# import time

# def start():
#     bar['value'] = 0
    
#     for i in range(1,11):
#         bar['value'] = i*10
#         window.update_idletasks()
#         time.sleep(0.5)
        
#     label.config(text="Task Done")    
# window = Tk()
# bar = Progressbar(window,orient=HORIZONTAL,length=200,mode='determinate')
# bar.pack()

# Button(text="click", command=start).pack()

# label = Label(window,text="") 
# label.pack()
# window.mainloop()


# ============================================================================

# from tkinter import *
# from tkinter.ttk import *
# import time


# def start_it():
#     bar.start(100)
#     label.config(text="Running")
#     time.sleep(1)
    
# def stop_it():
#     bar.stop()
#     label.config(text="Stopped")        

# window = Tk()

# bar = Progressbar(window, orient=HORIZONTAL, length=200, mode="determinate")
# bar.pack(padx=10, pady=10)

# frame = Frame(window)
# frame.pack()

# Button(frame,text="Start" , command=start_it).grid(row=0, column=0,padx=5)
# Button(frame,text="Stop" , command=stop_it).grid(row=0, column=1,padx=5)

# label = Label(window,text="waiting to start")
# label.pack(padx=10, pady=10)

# window.mainloop()

# =====================================================================================================================

from tkinter import *
from tkinter.ttk import *
import time

def start():
    # tasks = 10
    # x = 0
    # while x < tasks:
    #     time.sleep(0.5)
    #     bar['value'] += 10
    #     x += 1
    #     percent.set(str(int((x/tasks)*100))+"%")
    #     text.set(str(x)+"/"+str(tasks)+"Completed")
    #     window.update_idletasks()
    
    GB = 100
    download = 0
    speed = 3
    while download < GB:
        time.sleep(0.1)
        bar['value'] += (speed/GB)*100
        download += speed
        percent.set(str(int((download/GB)*100))+"%")
        text.set(str(download)+"/"+str(GB)+" GB Completed")
        window.update_idletasks()
    
window = Tk()

percent = StringVar()
text = StringVar()

bar = Progressbar(window,orient=HORIZONTAL,length=300,mode="determinate")
bar.pack()

percentlabel = Label(window,textvariable=percent)
percentlabel.pack()

tasklabel = Label(window,textvariable=text)
tasklabel.pack()

Button(text="Click", command=start).pack()

window.mainloop()