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

def eliminar():
    #crear conexion
    conexion = sqlite3.connect('direcciones.db')

    #cursor
    c = conexion.cursor()
    c.execute("DELETE FROM direccion WHERE oid="+codigo2.get())
    #commit cambios
    conexion.commit()

    #cerrar conexion
    conexion.close()
    pass


def enviar():
    
    #crear conexion
    conexion = sqlite3.connect('direcciones.db')

    #cursor
    c = conexion.cursor()
    c.execute("INSERT INTO direccion VALUES(:nombre, :apellido, :direccion, :codigo)",
                    {
                        'nombre': nombre.get(),
                        'apellido': apellido.get(),
                        'direccion': direccion.get(),
                        'codigo': codigo.get()
                    }
    )
    #commit cambios
    conexion.commit()

    #cerrar conexion
    conexion.close()

    
    nombre.delete(0, END)
    apellido.delete(0, END)
    direccion.delete(0, END)
    codigo.delete(0, END)
    
def consultar():
    #crear conexion
    conexion = sqlite3.connect('direcciones.db')

    #cursor
    c = conexion.cursor()
    
    c.execute("SELECT *, oid FROM direccion")
    datos = c.fetchall()
    print(datos)
    imprimir = ''
    for data in datos:
        imprimir += str(data[0])+" "+str(data[1])+" "+str(data[4])+"\n"
    
    texto = Label(root, text=imprimir)
    texto.grid(row=7, column=0)
    
     #commit cambios
    conexion.commit()

    #cerrar conexion
    conexion.close()

nombre = Entry(root, width=30)
nombre.grid(row=0, column=0, padx=20)
apellido = Entry(root, width=30)
apellido.grid(row=1, column=0, padx=20)
direccion = Entry(root, width=30)
direccion.grid(row=2, column=0, padx=20)
codigo = Entry(root, width=30)
codigo.grid(row=3, column=0, padx=20)

codigo2 = Entry(root, width=30)
codigo2.grid(row=4, column=0, padx=20)

nom = Label(root, text="nombre")
nom.grid(row=0, column=1)
ape = Label(root, text="apellido")
ape.grid(row=1, column=1)

dire = Label(root, text="direccion")
dire.grid(row=2, column=1)

cod = Label(root, text="codigo")
cod.grid(row=3, column=1)
cod2 = Label(root, text="ID")
cod2.grid(row=4, column=1)

btn = Button(root, text="agregar", width=25, command=enviar)
btn.grid(row=5, columnspan=2, padx=10)

btn2 = Button(root, text="mostrar", width=25, command=consultar)
btn2.grid(row=6, columnspan=2, padx=20)

btn3 = Button(root, text="eliminar", width=25, command=eliminar)
btn3.grid(row=10, columnspan=2, padx=20)



root.mainloop()