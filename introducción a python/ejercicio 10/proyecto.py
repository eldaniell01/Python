import random
#el primero a 3 gana
count = 0
ganador1= 0
ganadar2 = 0
options = ('piedra','papel', 'tijera')
while count < 5:
    count +=1
    print('ronda No.', count)
    if ganadar2 == 3 or ganador1 == 3:
        if ganador1 > ganadar2:
            print("gana el usuario")
            break
        else:
            print("gana el computador")
    option = input('piedra papel o tijera ')
    option = option.lower()
    computadora = random.choice(options)
    if option in options:
        print('Usuario', option)
        print('computadora', computadora)

        if option == computadora:
            count -=1
            print("empate, vuelva intentarlo de nuevo")
        elif option == 'piedra':
            if computadora == 'tijera':
                print('gana  usuario')
                ganador1 +=1
            else:
                ganadar2 += 1
                print('gana computadora')
                
        elif option == 'papel':
            if computadora == 'piedra':
                print('usuario gana')
                ganador1 +=1
            else:
                ganadar2 += 1
                print('computadora gana')
        elif option == 'tijera':
            if computadora == 'papel':
                print('gana usuario')
                ganador1 +=1
            else:
                ganadar2 += 1
                print('computadora gano')
        else:
            print('error en la eleccion')
        
    else:
        count -=1
        print('opción incorrecta')
    