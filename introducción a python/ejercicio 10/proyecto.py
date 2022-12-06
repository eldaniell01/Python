option = input('piedra papel o tijera ')
option = option.lower()
computadora = 'piedra'
if option == computadora:
    print("empate")
elif option == 'piedra':
    if computadora == 'tijera':
        print('gana  usuario')
    else:
        print('gana computadora')
        
elif option == 'papel':
    if computadora == 'piedra':
        print('usuario gana')
    else:
        print('computadora gana')
elif option == 'tijera':
    if computadora == 'papel':
        print('gana usuario')
    else:
        print('computadora gano')
else:
    print('error en la eleccion')