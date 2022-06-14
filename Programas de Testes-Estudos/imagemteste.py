from tkinter import *
from PIL import Image, ImageTk

root = Tk()

image = Image.open('cal.png')
image = image.resize((100, 100))

photo = ImageTk.PhotoImage(image)
label = Label(image=photo)
label.image = photo 
label.pack()

root['bg'] = 'blue'
root.mainloop()
