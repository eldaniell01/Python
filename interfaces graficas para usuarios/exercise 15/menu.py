from tkinter import *
from PIL import ImageTk, Image
from tkinter import filedialog
root = Tk()
root.title('check')
root.geometry("800x600")
options=[
    "lunes", 
    "martes",
    "miercoles"
]
click = StringVar()
click.set(options[0])

def mostrar():
    mos = Label(root, text=click.get()).pack()
menu = OptionMenu(root, click, *options)
menu.pack()

btn = Button(root, text="seleccionar", command=mostrar).pack()
root.mainloop()