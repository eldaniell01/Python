from tkinter import *
from PIL import ImageTk, Image
from tkinter import filedialog
import sqlite3
root = Tk()
root.title('base de datos')
root.geometry("800x600")

#crear conexion
conexion = sqlite3.connect('direcciones.db')

#cursor
c = conexion.cursor()
#crear tabla
c.execute("""
          CREATE TABLE direccion(
              nombre text,
              apellido text,
              direccion text,
              codigo integer
          )
          """)

#commit cambios
conexion.commit()

#cerrar conexion
conexion.close()

root.mainloop()