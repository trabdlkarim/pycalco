import click
from pycalco.calculator import PyCalco

calc = PyCalco()

@click.group()
def run():
    pass
    

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
