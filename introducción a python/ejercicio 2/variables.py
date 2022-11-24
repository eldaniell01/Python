"""
crear variables
"""
my_name = "daniel"
print(my_name)
last_name = "montepeque"
print("aqui esta de nuevo", my_name)
print("uniendo palabras", my_name+" "+last_name)
print("uniendo letras",my_name[2]+ last_name[4])
print("separar con caracteres",my_name, last_name, sep="--")

"""
    asignación de valor en tiempo de ejecución
"""
my_name = input("su nombre: ")

print("el nombre es ", my_name)