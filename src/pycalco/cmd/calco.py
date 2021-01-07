import click

from pycalco import version
from pycalco.calculator import PyCalco

calc = PyCalco()

@click.group(invoke_without_command=True)
@click.pass_context
@click.version_option(version=version, prog_name="PyCalco")
@click.option("--interactive", '-i', is_flag=True, help="Synonym or alias for launch command")
def run(ctx, interactive):
    if interactive:
        calc.run()
        exit(0)
    elif not ctx.invoked_subcommand:
        calc.run()
    
@run.command()
@click.argument('expr', nargs=-1)
def eval(expr):
    """Evaluate arthimetically given expression"""
    calc.exec('eval ' + "".join(expr))

@run.command()
@click.argument('expr', nargs=-1)
def sym(expr):
    """Compute symbolically given expression"""
    calc.exec('sym ' + "".join(expr))

@run.command()
def launch():
    """Launch PyCalco in interactive mode"""
    calc.run()


if __name__ == '__main__':
    run(obj={})
