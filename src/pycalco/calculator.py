"""This module is a collection of classes and 
operations for the arithmetic expressions that 
will come as input from the end user.
"""

import sys
import click

from pycalco.shell  import PyCalcoShell

class PyCalco(object):
    def __init__(self):
        self.shell = PyCalcoShell()
    
    def eval(self, expression):
        pass 
    
    def sym(self, args):
        pass
    
    @click.command()
    @click.option('--count/-c', default=1, help='Number of greetings.')
    @click.argument('name')
    def run(self, count, name):
        for i in range(count):
            click.echo('Hi there, '+name)



