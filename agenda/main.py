
from http import client
from pydoc import cli

from torch import true_divide

import sys

clientes = 'daniel,kevin,'

def create_cliente(cliente_name):
    global clientes
    if cliente_name not in clientes:
        clientes+=cliente_name
        
        _add_comma()
    else:
        print('ya se encuentra en la lista de cliente\'s')
    
def list_clientes():
    global clientes
    print(clientes)

def update_cliente(cliente_name, update_cliente_name):
    global clientes
    if cliente_name in clientes:
        clientes=clientes.replace(cliente_name+',', update_cliente_name +',')
    else:
        print('cliente no encontrado')

def delete_cliente(cliente_name):
    global clientes
    if cliente_name in clientes:
        clientes = clientes.replace(cliente_name+',', '')
    else:
        print('cliente no encontrado')

def search(cliente_name):
    lista_clientes = clientes.split(',')
    for cliente in lista_clientes:
        if cliente != cliente_name:
            continue
        else:
            return True
        
def _add_comma():
    global clientes
    clientes+=', '

def bienvenida():
    print('Bienvenidos')
    print('*'*50)
    print('selecciona una opción')
    print('[C] crear cliente')
    print('[U] actualizar cliente')
    print('[D] eliminar cliente')
    print('[S] buscar')
    print('[E] salir')

def _get_cliente():
    client_name = None
    while not client_name:
        client_name=input('escribe el nombre del cliente: ')
        if client_name=='exit':
            client_name=None
            break
    if not client_name:
        sys.exit()
    return client_name

if __name__ == '__main__':
    bienvenida()
    commando = input()
    commando=commando.upper()
    while commando!='E':
        if commando =='C':
            cliente_name = _get_cliente()
            create_cliente(cliente_name)
            list_clientes()
            
        elif commando =='D':
            cliente_name =_get_cliente()
            delete_cliente(cliente_name)
            list_clientes()
            
        elif commando=='U':
            cliente_name = _get_cliente()
            update_name=input('nombre actualizado ')
            update_cliente(cliente_name, update_name)
            list_clientes()
            
        elif commando=='S':
            cliente_name =_get_cliente()
            found =search(cliente_name)
            if found:
                print('el cliente esta ')
            else:
                print('no encontrado: {}'.format(cliente_name))
        
        bienvenida()
        commando = input()
        commando=commando.upper()
    