import random
#el primero a 3 gana


def choiseOption():
    options = ('piedra','papel', 'tijera')
    option = input('piedra papel o tijera ')
    option = option.lower()
    computadora = random.choice(options)
    return option, computadora, options


def reglas(usuario, computadora, opcion, count, ganador1, ganador2):
    if usuario in opcion:
        print('Usuario', usuario)
        print('computadora', computadora)

        if usuario == computadora:
            count -=1
            
            print("empate, vuelva intentarlo de nuevo")
        elif usuario == 'piedra':
            if computadora == 'tijera':
                print('gana  usuario')
                ganador1 +=1
            else:
                ganador2 += 1
                print('gana computadora')
                
        elif usuario == 'papel':
            if computadora == 'piedra':
                print('usuario gana')
                ganador1 +=1
            else:
                ganador2 += 1
                print('computadora gana')
        elif usuario == 'tijera':
            if computadora == 'papel':
                print('gana usuario')
                ganador1 +=1
            else:
                ganador2 += 1
                print('computadora gano')
        else:
            print('error en la eleccion')
        
    else:
        count -=1
        print('opción incorrecta')
    return count, ganador1, ganador2    
        
def game():
    ganador1= 0
    ganador2 = 0
    count = 0
    while count < 5:
        count +=1
        print('*'*15)
        print('ronda No.', count)
        print('*'*15)
        option, computadora, options = choiseOption()
        count, ganador1, ganador2= reglas(option, computadora, options, count, ganador1, ganador2)
        print("usuario:", ganador1)
        print("computadora:", ganador2)
        if ganador2 == 3 or ganador1 == 3:
            if ganador1 > ganador2:
                print("gana el usuario")
                break
            else:
                print("gana el computador")
                break
        print('*'*15)

game()
                
