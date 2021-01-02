#!/usr/bin/env python3

import sys
from pycalco.shell import PyCalcoShell

def main(argv):
    shell = PyCalcoShell()
    shell.cmdloop()
    

if __name__ == "__main__":
    main(sys.argv[1:])
