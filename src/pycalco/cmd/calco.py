import click

from pycalco import version
from pycalco.calculator import PyCalco

calc = PyCalco()

@click.group()
@click.option("--version/-v", default=False, help="Print PyCalco version")
def run():
    click.echo(version)
    

@run.command()
@click.argument('expr')
def eval(expr):
    calc.exec('eval ' + expr)

@run.command()
@click.argument('expr')
def sym(expr):
    calc.exec('sym ' + expr)

if __name__ == '__main__':
    run()
