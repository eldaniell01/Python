from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title('ventanas')

def open():
    global img
    top = Toplevel()
    top.title('nueva ventana')
    img = ImageTk.PhotoImage(Image.open("interfaces graficas para usuarios/exercise 11/wallpaper_1.jpg"))
    mostrar = Label(top, image=img, width=100, height=100).pack()
    btn2 = Button(top, text="cerrar", command=top.destroy).pack()
    
btn = Button(root, text='abrir', command=open).pack()

root.mainloop()