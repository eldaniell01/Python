#file = open("comprehensions, funciones y manejo de errores/ejercicio 24/text.txt")
#print(file.read())
#print(file.readline())
#for i in file:
#    print(i)
#file.close()

with open("comprehensions, funciones y manejo de errores/ejercicio 24/text.txt") as file:
    for line in file:
        print(line)