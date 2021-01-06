GREEN = '\033[92m'
RED = '\033[31m'
END = '\033[0m'
VER = '0.9.1'

from . import aux
from . import calculator as calc
from . import shell

def main():
    """Entry point for the application script"""
    calco = calc.Calco()
    calco.run()
