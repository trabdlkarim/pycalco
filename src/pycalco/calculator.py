"""This module is a collection of classes and 
operations for the arithmetic expressions that 
will come as input from the end user.
"""

import pycalco
from pycalco.shell  import PyCalcoShell

class PyCalco(object):
    def __init__(self):
        self.version = pycalco.version
        self.shell = PyCalcoShell()
    
    def exec(self, cmd):
        self.shell.onecmd(cmd) 
    
    def run(self):
        self.shell.cmdloop()
