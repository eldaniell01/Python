
from random import random, randint

from torch import le


imagenes = ['''
            +---+
            |   |
                |
                |
                |
                |
                =========''','''
            +---+
            |   |
            0   |
                |
                |
                |
                ==========''','''
            +---+
            |   |
            0   |
            |   |
                |
                |
                ==========''','''
            +---+
            |   |
            0   |
           /|   |
                |
                |
                ==========''','''
            +---+
            |   |
            0   |
           /|\  |
                |
                |
                ==========''','''
            +---+
            |   |
            0   |
           /|\  |
            |   |
                |
                ==========''','''
            +---+
            |   |
            0   |
           /|\  |
            |   |
           /    |
                ==========''','''
            +---+
            |   |
            0   |
           /|\  |
            |   |
           / \  |
                ==========''','''''']

palabras =[
    'lavadora',
    'hola',
    'teclado'
]

def display(palabra_escondida, tries):
    print(imagenes[tries])
    print('')
    print(palabra_escondida)
    print("----*----*----*----*----*----")


def randow_word():
    id = randint(0, len(palabras)-1)
    return palabras[id]

def run():
    word = randow_word()
    palabra_escondida=['-'] * len(word)
    tries=0
    while True:
        display(palabra_escondida, tries)
        letra=input("escribe una letra: ")
        
        id_letra=[]
        
        for idx in range(len(word)):
            if word[idx] == letra:
                id_letra.append(idx)
        
        if len(id_letra)==0:
            tries+=1
            if tries ==7:
                display(palabra_escondida, tries)
                print('perdiste la palabra correcta era {}'.format(word))
                break
            
        else:
            for idx in id_letra:
                palabra_escondida[idx]=letra
            id_letra=[]
            
        try:
            palabra_escondida.index('-')
        except ValueError:
            print('')
            print('terminado')
if __name__=='__main__':
    print('bienvenidos')
    run()