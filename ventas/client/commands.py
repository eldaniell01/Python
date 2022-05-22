from multiprocessing.connection import Client
from pydoc import cli
import click
from prompt_toolkit import prompt
from client.services import Servicio_cliente
from client.modelo import Model_cliente

@click.group()
def cliente():
    """son los cliente
    """


@cliente.command()
@click.option('-n', 
              '--name',
              type=str,
              prompt=True,
              help='Nombre del cliente')
@click.option('-t', 
              '--trabajo',
              type=str,
              prompt=True,
              help='trabajo del cliente')
@click.option('-e', 
              '--email',
              type=str,
              prompt=True,
              help='email del cliente')

@click.pass_context
def create(ctx, name, trabajo, email):
    """sirve para crear un cliente

    Args:
        ctx (_type_): _description_
        name (_type_): _description_
        trabajo (_type_): _description_
        email (_type_): _description_
    """
    cliente = Model_cliente(name, trabajo, email)
    cliente_servicio = Servicio_cliente(ctx.obj['cliente_table'])
    cliente_servicio.create_cliente(cliente)


@cliente.command()
@click.pass_context   
def lista(ctx):
    """lista de clientes

    Args:
        ctx (_type_): _description_
    """
    cliente = Servicio_cliente(ctx.obj['cliente_table'])
    lista_cliente = cliente.list_cliente()
    click.echo('ID       |       NAME        |       TRABAJO     |       EMAIL')
    click.echo('*'*100)
    for client in lista_cliente:
        click.echo('{idx}        |       {name}      |       {trabajo}       |       {email}'.format(
            idx = client['idx'],
            name = client['name'],
            trabajo = client['trabajo'],
            email = client['email']
        ))


@cliente.command()
@click.argument('cliente_id',
                type=str)
@click.pass_context       
def actualizar(ctx, cliente_id):
    """actualiza clientes

    Args:
        ctx (_type_): _description_
        cliente_id (_type_): _description_
    """
    cliente_servicio = Servicio_cliente(ctx.obj['cliente_table'])
    clientes = cliente_servicio.list_cliente()
    clients = [clients for clients in clientes if clients['idx'] == cliente_id]
    if clients:
        clients = update(Model_cliente(**clients[0]))
        cliente_servicio.update_cliente(clients)
        click.echo('cliente actualizado')
    else:
        click.echo('cliente no actualizado')

def update(clients):
    click.echo('dejar en blanco los datos que no se quieren modificar')
    clients.name=click.prompt('nuevo nombre ', type=str, default=clients.name)
    clients.trabajo=click.prompt('nuevo trabajo ', type=str, default=clients.trabajo)
    clients.email=click.prompt('nuevo email ', type=str, default=clients.email)
    return clients

@cliente.command()
@click.argument('cliente_id',
                type=str)
@click.pass_context       
def eliminar(ctx, cliente_id):
    """elimina clientes 

    Args:
        ctx (_type_): _description_
        cliente_id (_type_): _description_
    """
    cliente_servicio = Servicio_cliente(ctx.obj['cliente_table'])
    if click.confirm('seguro que deseas eliminar este id: {}'.format(cliente_id)):
        cliente_servicio.delete_clientes(cliente_id)

all = cliente