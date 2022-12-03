if True:
    print("hola mundo")
    
if False:
    print("hola dos")


pet = input("el nombre de mi mascota es ")

if pet == "gato":
    print("es mi mascota")
elif pet =="perro":
    print("no es mi mascota")
elif pet == "pez":
    print("otro")    
else: 
    print("incorrecto")

stock = int(input("ingrese el stock "))

if stock >=100 and stock<=1000:
    print('es correcto')
else:
    print("es incorrecto") 