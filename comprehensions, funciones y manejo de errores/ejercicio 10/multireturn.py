def volumen(length, width, depth):
    return length* width* depth

result = volumen(10, 20, 14)
print(result)

def volumen2(length=1, width=1, depth=1):
    return length* width* depth

result = volumen2()
print(result)

def volumen3(length=1, width=1, depth=1):
    return length* width* depth

result = volumen3(width=20)
print(result)

def volumen4(length=1, width=1, depth=1):
    return length* width* depth, width, 'hola'

result = volumen4(width=20)
print(result)

def volumen5(length=1, width=1, depth=1):
    return length* width* depth, width, 'hola'

result, ancho, texto= volumen5(width=20)
print(result)
print(ancho)
print(texto)
