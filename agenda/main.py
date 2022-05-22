
from http import client
from pydoc import cli

from torch import true_divide
import csv
import os
import sys

tabla_clientes='.clientes.csv'
schema_clientes=['name', 'trabajo', 'email']
clientes = []

def iniciacion():
    with open(tabla_clientes, mode='r') as f:
        leer = csv.DictReader(f, fieldnames=schema_clientes)
        
        for row in leer:
            clientes.append(row)
        
def guardar_cliente():
    tmp_table = '{}.tmp'.format(tabla_clientes)
    with open(tmp_table, mode='w') as f:
        escribir = csv.DictWriter(f, fieldnames=schema_clientes)
        escribir.writerows(clientes)
        f.close()
        os.remove(tabla_clientes)
        os.rename(tmp_table, tabla_clientes)
        

def create_cliente(cliente):
    global clientes
    if cliente not in clientes:
        clientes.append(cliente)
    else:
        print('ya se encuentra en la lista de cliente\'s')
    
def list_clientes():
    print('id   |   name    |   trabajo     |   email')
    print('*'*50)
    for idx, cliente in enumerate(clientes):
        print('{id} | {name} | {trabajo} | {email}'.format(
            id = idx,
            name = cliente['name'],
            trabajo = cliente['trabajo'],
            email = cliente['email']
        ))

def update_cliente(cliente_id, update_cliente_name):
    global clientes
    if len(clientes)-1>=cliente_id:
        clientes[cliente_id] = update_cliente_name
    else:
        print('cliente no encontrado')

def delete_cliente(cliente_id):
    global clientes
    for idx, cliente in enumerate(clientes):
        if idx == cliente_id:
            del clientes[idx]
            break
        else:
            print('cliente no encontrado')

def search(cliente_name):
    
    for cliente in clientes:
        if cliente['name'] != cliente_name:
            continue
        else:
            return True

def bienvenida():
    print('Bienvenidos')
    print('*'*50)
    print('selecciona una opción')
    print('[C] crear cliente')
    print('[L] listar clientes')
    print('[U] actualizar cliente')
    print('[D] eliminar cliente')
    print('[S] buscar')
    print('[E] salir')

def _get_cliente_objeto(objeto_name):
    field = None
    while not field:
        field = input('datos del cliente: {} '.format(objeto_name))
    return field
        
def _get_cliente():
    client = {
        'name': _get_cliente_objeto('name'),
        'trabajo': _get_cliente_objeto('trabajo'),
        'email': _get_cliente_objeto('email')
    }
    return client

if __name__ == '__main__':
    iniciacion()
    bienvenida()
    commando = input()
    commando=commando.upper()
    while commando!='E':
        if commando =='C':
            cliente = _get_cliente()
            create_cliente(cliente)
            
            
        elif commando =='D':
            cliente_id = int(_get_cliente_objeto('id'))
            delete_cliente(cliente_id)
            
            
        elif commando=='U':
            cliente_id = int(_get_cliente_objeto('id'))
            updated_cliente = _get_cliente()
            update_cliente(cliente_id, updated_cliente)
            
            
        elif commando=='S':
            cliente_name = _get_cliente_objeto('name')
            found =search(cliente_name)
            if found:
                print('el cliente esta ')
            else:
                print('no encontrado: {}'.format(cliente_name))
        elif commando =='L':
            list_clientes()
        bienvenida()
        commando = input()
        commando=commando.upper()
    guardar_cliente()