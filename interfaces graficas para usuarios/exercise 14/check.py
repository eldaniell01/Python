from tkinter import *
from PIL import ImageTk, Image
from tkinter import filedialog
root = Tk()
root.title('check')
root.geometry("800x600")

var = StringVar()

c = Checkbutton(root, text="dale aqui", variable=var, onvalue="On", offvalue="Off")
c.deselect()
c.pack()

def check():
    mostrar = Label(root, text=var.get()).pack()
    
btn = Button(root, text="mostrar", command=check).pack()

root.mainloop()