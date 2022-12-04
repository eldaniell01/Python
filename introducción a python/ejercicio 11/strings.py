text = "ella sabe programar en python"

"""
    métodos de string
1.	capitaliza      Cambia todas las letras a minúsculas menos la primera.
2.	casefold        Utilizada para compara cadenas sin importar el tamaño de los caracteres.
3.  center          Formaseta una cadena alineandola al centro
4.  count           Cuenta las ocurrencias de una cadena
5.  encode          Codifica una cadena según la codificación deseada.
6.  endswith        Comprueba si la cadena termina con una cadena específica.
7.  expandtabs      Convierte los tabuladores en espacios.
8.  find            Devuelve el índice de la cadena buscada o -1 si no se encuentra.
9.  format          Formatea una cadena de forma avanzada.
10. format_map      Igual que format, pero sin hacer una copia de los parámetros.
11. index           Devuelve el índice de una cadena de caracteres o ValueError.
12. isalnum         Comprueba si la cadena es alfanumérica.
13. isalpha         Comprueba si la cadena es alfabética.
14. isascci         Comprueba si la cadena es ASCII.
15. isdecimal       Comprueba si la cadena es un decimal.
16. isdigit         Comprueba si la cadena es un dígito.
17. isidentifier    Comprueba si la cadena es un identificador.
18. islower         Comprueba si todos los caracteres son minúsculos.
19. isnumeric       Comprueba si la cadena es numérica.
20. isprintable     Comprueba si la cadena es imprimible.
21. isspace         Comprueba si la cadena solo contiene espacios.
22. istitle         Comprueba si la cadena tiene formato de título.
23. isupper         Comprueba si todos los caracteres son mayúsculas.
24. join            Une todos los elementos de un iterador en una cadena.
25. ljust           Justifica la cadena a la izquierda.
26. lower           Convierte la cadena a minúsculas.
27. lstrip          Elimina los caracteres de espacio de la izquierda.
28. maketrans       Crea una tabla de traducción para translate.
29. partition       Crea particiones de una cadena usando un separador.
30. replace         Reemplaza en la misma cadena un carácter por otro.
31. removeprefix    Devuelve una nueva cadena con el prefijo especificado como argumento eliminado si se encuentra en la cadena origina.
32. removesuffix    Devuelve una nueva cadena con el sufijo especificado
33. rfin            Devuelve el índice de la cadena como parámetro buscando por la derecha o -1 si no se encuentra.
34. rindex          Devuelve el índice de la cadena como parámetro buscando por la derecha o ValueError.
35. rjust           Justifica la cadena a la derecha.
36. rpartition      Crea particiones de una cadena usando un separador y comenzando por la derecha.
37. rsplit          Devuelve una lista de cadenas al separar la original por un separador buscando por la derecha.
38. rstrip          Devuelve una lista de cadenas separando la original por saltos de línea.
39. split           Devuelve una lista de cadenas al separar la original por un separador.
40. splitlines      Devuelve una lista de cadenas separando la original por saltos de línea.
41. startswith      Comprueba si la cadena comienza con una cadena específica.
42. strip           Elimina los espacios iniciales y finales de la cadena.
43. swapcase        Cambia el tamaño de cada letra de minúsculas a Mayúsculas y las que estan en Mayúsculas a minúsculas.
44. title           Convierte la cadena a formato título.
45. translate       Reemplaza cada carácter por otro siguiendo una tabla de traducciones.
46. upper           Convierte la cadena a mayúsculas.
47. zfill           Añade ceros a la izquierda a una cadena numérica.
"""

"""
    in: permite comprobar si se encuentra un texto dentro de la cadena de texto
"""

print('javascript' in text)
print('en' in text)

if 'enrtr' in text:
    print('esta')
else:
    print('no esta')


"""
    len: obtiene el tamaño del string(cuenta también los espacios)
"""

size = len('es amor')
print(size)

"""
    upper: pasa todo el texto a mayusculas
"""
print(text, text.upper())
"""
    lower: pasa todo el texto a minusculas
"""
print(text, text.lower())

"""
    count: cuenta la cantidad de veces que se repite una letra
"""
print(text, text.count('a'))

"""
    swapcase: todo lo que este a mayuscula pasa a minuscula y de minuscula a mayuscula
"""
print(text, text.swapcase())

"""
    startswitch: busca si se encuentra el texto solicitado al principio del texto 
"""
print(text, text.startswith('ella'))

"""
    endswitch: busca si se encuentra el texto solicitado al final del texto 
"""
print(text, text.endswith('ella'))

"""
    replace: cambia el texto por otro
"""
print(text, text.replace('python', 'java'))

"""
    capitalize: pone el primer caracter en mayuscula
"""
print(text, text.capitalize())

"""
    title: pone las iniciales de cada palabra del texto en mayusculas
"""
print(text, text.title())

"""
    isdigit: comprueba si la cadena de texto son digitos
"""
print(text, text.isdigit())