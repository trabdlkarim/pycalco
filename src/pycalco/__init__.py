
version = '0.9.1'

from . import aux
from . import cmd
from . import calculator
from . import shell

def main():
    """Entry point for the application script"""
    cmd.calco.run(obj={})
