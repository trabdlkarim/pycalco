
import click

@click.command()
@click.option('--count/-c', default=1, help='Number of greetings.')
@click.argument('name')
def run(count, name):
    for i in range(count):
        click.echo('Hi there, '+name)


def eval(expr):
    pass

def sym(expr):
    pass
