import click

from pycalco import version as ver
from pycalco.calculator import PyCalco

calc = PyCalco()

@click.group(invoke_without_command=True)
@click.pass_context
@click.option("--version", "-v", default=False, help="Print PyCalco version")
def run(ctx, version):
    if version:
        click.echo(ver)
        exit(0)
    elif ctx.invoked_subcommand is None:
        calc.run()
    
@run.command()
@click.argument('expr')
def eval(expr):
    """Evaluate arthimetically given expression"""
    calc.exec('eval ' + expr)

@run.command()
@click.argument('expr')
def sym(expr):
    """Compute symbolically given expression"""
    calc.exec('sym ' + expr)

@run.command()
def launch():
    """Launch PyCalco in interactive mode"""
    calc.run()


if __name__ == '__main__':
    run(obj={})
