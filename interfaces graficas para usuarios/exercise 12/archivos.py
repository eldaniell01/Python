from tkinter import *
from PIL import ImageTk, Image
from tkinter import filedialog
root = Tk()
root.title('frames')

def open(): 
    global img
    root.filename = filedialog.askopenfilename(initialdir="interfaces graficas para usuarios", title="seleccionar archivo", filetypes=(("png files", "*.jpg"),("all files", "*.*")))
    img = ImageTk.PhotoImage(Image.open(root.filename))
    mostrar = Label(root, image=img, width=100, height=100).pack()

btn = Button(root, text="abrir archivo", command=open).pack()

root.mainloop()