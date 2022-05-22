import click
from client import commands as comandos_clientes

clientes_table = '.clientes.csv'

@click.group()
@click.pass_context
def cli(ctx):
    ctx.obj = {}
    ctx.obj['cliente_table']=clientes_table

cli.add_command(comandos_clientes.all)