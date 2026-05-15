from tkinter import *
from PIL import Image, ImageTk

window = Tk()

photo = Image.open('download.jpg')
res = photo.resize((150,150), Image.Resampling.LANCZOS)
image_tk = ImageTk.PhotoImage(res)

label = Label(window,
              text="Hi This is Nishwa!",
              bg='green',
              fg='red',
              relief=RAISED,
              bd=10,
              padx=10,
              pady=10,
              image=image_tk,
              compound='top')

# label.image = image_tk
label.pack()

window.mainloop()
