from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title('scroll')
root.geometry("800x600")

vertical = Scale(root, from_=0, to = 200)
vertical.pack()


def barra():
    mostrar = Label(root, text=horizontal.get()).pack()
    root.geometry(str(horizontal.get())+"x"+str(vertical.get()))
    
    
    
horizontal = Scale(root, from_=0, to= 200, orient=HORIZONTAL, command=barra)
horizontal.pack()
mostrar = Label(root, text=horizontal.get()).pack()


btn  = Button(root, text="tamaño", command=barra).pack()

root.mainloop()