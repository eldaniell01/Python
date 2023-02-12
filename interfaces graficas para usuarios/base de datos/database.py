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
    
def save():
    #crear conexion
    conexion = sqlite3.connect('direcciones.db')
    key = codigo2.get()
    #cursor
    c = conexion.cursor()
    c.execute("""UPDATE direccion SET
              nombre = :nombre,
              apellido = :apellido,
              direccion = :direccion,
              codigo = :codigo
              
              WHERE oid= :oid""",
              {
                  'nombre': nombre_act.get(),
                  'apellido': apellido_act.get(),
                  'direccion': direccion_act.get(),
                  'codigo': codigo_act.get(),
                  'oid': key
              }
              )
    
    
    
    #commit cambios
    conexion.commit()

    #cerrar conexion
    conexion.close()
    act.destroy()
    

def actualizar():
    global act
    act = Tk()
    act.title('base de datos')
    act.geometry("800x600")
    
    #crear conexion
    conexion = sqlite3.connect('direcciones.db')

    #cursor
    c = conexion.cursor()
    
    key = codigo2.get()
    
    c.execute("SELECT * FROM direccion WHERE oid="+key)
    datos = c.fetchall()
    
    global nombre_act
    global apellido_act
    global direccion_act
    global codigo_act
    global codigo2_act
    
    
    nombre_act = Entry(act, width=30)
    nombre_act.grid(row=0, column=0, padx=20)
    apellido_act = Entry(act, width=30)
    apellido_act.grid(row=1, column=0, padx=20)
    direccion_act = Entry(act, width=30)
    direccion_act.grid(row=2, column=0, padx=20)
    codigo_act = Entry(act, width=30)
    codigo_act.grid(row=3, column=0, padx=20)

    codigo2_act = Entry(act, width=30)
    codigo2_act.grid(row=4, column=0, padx=20)

    nom_act = Label(act, text="nombre")
    nom_act.grid(row=0, column=1)
    ape_act = Label(act, text="apellido")
    ape_act.grid(row=1, column=1)

    dire_act = Label(act, text="direccion")
    dire_act.grid(row=2, column=1)

    cod_act = Label(act, text="codigo")
    cod_act.grid(row=3, column=1)
    cod2_act = Label(act, text="ID")
    cod2_act.grid(row=4, column=1)
    
    for lista in datos:
        nombre_act.insert(0, lista[0])
        apellido_act.insert(0, lista[1])
        direccion_act.insert(0, lista[2])
        codigo_act.insert(0, lista[3])
        codigo2_act.insert(0, key)
 
    
    btn4_act = Button(act, text="actualizar", width=25, command=save)
    btn4_act.grid(row=11, columnspan=2, padx=20)


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

btn4 = Button(root, text="actualizar", width=25, command=actualizar)
btn4.grid(row=11, columnspan=2, padx=20)

root.mainloop()