import click

from pycalco import version as ver
from pycalco.calculator import PyCalco

calc = PyCalco()

@click.group()
@click.option("--version/-v", default=False, help="Print PyCalco version")
@click.option("--interactive/-i", default=True, help="Lauch PyCalco in interactive mode")
def run(version,interactive):
    if version:
        click.echo(ver)
    else if interactive:
        calc.run()?
    
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
