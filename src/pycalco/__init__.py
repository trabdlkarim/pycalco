
version = '0.9.1'

from . import aux
from . import calculator
from . import shell

def run():
    """Entry point for the application script"""
    calco = calculator.PyCalco()
    calco.run()
