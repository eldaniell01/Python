"""
    indexing: significa que cada una de las letras o caracteres del texto tiene un indicador
    o indice al cual se puede ingresar a nivel de posiciones
"""
text = "hola mundo"
print(text[0])
print(text[1])

size = len(text)
print(text[size-1])

"""
    al agregarle el signo '-' comienza a contar desde el final hacia el principio
"""
print(text[-1])

"""
    slicing: se puede ingresar a partes del texto
"""
print(text[0:5])
print(text[:6])
print(text[:8])
print(text[3:])
print(text[::2])
print(text[::4])