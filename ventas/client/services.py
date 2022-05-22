import csv
from client.modelo import Model_cliente
import os

from requests import delete
class Servicio_cliente:
    def __init__(self, table_name):
        self.table_name = table_name
    
    def create_cliente(self, cliente):
        with open(self.table_name, mode='a') as f:
            write = csv.DictWriter(f, fieldnames=Model_cliente.schema())
            write.writerow(cliente.to_dict())
    
    def list_cliente(self):
        with open(self.table_name,  mode='r') as f:
            reader = csv.DictReader(f, fieldnames=Model_cliente.schema())
            return list(reader)
    
    def update_cliente(self, cliente):
        clientes = self.list_cliente()
        update = []
        for client in clientes:
            if client['idx'] == cliente.idx:
                update.append(cliente.to_dict())
            else:
                update.append(client)
        self.guardar(update)
        
    def guardar(self, clientes):
        tmp_table_name = self.table_name + '.tmp'
        with open(tmp_table_name, mode='w') as f:
            write = csv.DictWriter(f, fieldnames=Model_cliente.schema())
            write.writerows(clientes)
            f.close()
        os.remove(self.table_name)
        os.rename(tmp_table_name, self.table_name)
    
    
    def delete_clientes(self, cliente):
        clientes = self.list_cliente()
        delete = [client for client in clientes if client['idx']!= cliente]
        self.guardar(delete)