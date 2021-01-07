import click

@click.command()
@click.option('--count/-c', default=1, help='Number of greetings.')
@click.argument('name')
def run(self, count, name):
    for i in range(count):
        click.echo('Hi there, '+name)

