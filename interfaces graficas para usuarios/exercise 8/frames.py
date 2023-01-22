from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title('frames')
frm = LabelFrame(root, text="framaaasaes", padx=50, pady=50)
frm.pack(padx=100, pady=100)

b = Button(frm, text='0hoal')
b.pack()

root.mainloop()