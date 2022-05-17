
import numbers
import re


def buscar_numero(numbers, num, inicio, fin):
    if inicio>fin:
        return False
    medio = int((inicio+fin)/2)
    if numbers[medio]== int(num):
        return True
    elif numbers[medio] > int(num):
        print(numbers[medio])
        return buscar_numero(numbers, num, inicio, medio-1)
    else:
        print(numbers[medio])
        return buscar_numero(numbers, num, medio+1, fin)


if __name__ =='__main__':
    numbers =[1,2,3,4,5,6,7,8,9]
    num = int(input("ingrese el numero: "))
    
    result = buscar_numero(numbers, num, 0, len(numbers)-1)
    
    if result is True:
        print('si se encontro')
    else:
        print('no se econtro')