from torch import le


def caracter_no_repetido(word):
    letter ={}
    for idx, letr in enumerate(word):
        if letr not in letter:
            letter[letr]=(idx, 1)
        else:
            letter[letr]=(letter[letr][0], letter[letr][1]+1)
    final_letter =[]
    for key, value in letter.items():
        if value[1] == 1:
            final_letter.append((key, value[0]))
    no_repetir = sorted(final_letter, key=lambda value: value[1])
    
    if no_repetir:
        return no_repetir[0][0]
    else:
        return '_'

if __name__ == '__main__':
    word = str(input('escribe una secuencia de letras: '))
    result = caracter_no_repetido(word)
    
    if result=='_':
        print('todos los caracteres se repiten')
    else:
        print('el caracter no repetido es: {}'.format(result))