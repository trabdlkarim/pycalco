import sys
import math
import cmd
import re

import click


GREEN = '\033[92m'
RED = '\033[31m'
END = '\033[0m'
VERSION = "0.9.0"

GLOBALS = {}
  
class PyCalcoShell(cmd.Cmd):
    intro = "\nWelcome to PyCalco shell.\n"
    intro += "Type 'help' or '?' to list all available commands.\n"
    intro += "PyCalco " + VERSION + " -- A Powerful Python Arithmetic Calculator\n\n"
    prompt = GREEN + "PyCalco [%i]: " + END
    
    def preloop(self):
        self.cmd_count = 1
        PyCalcoShell.prompt = PyCalcoShell.prompt % self.cmd_count 
    
    def precmd(self,line):
        self.cmd_count += 1
        PyCalcoShell.prompt = GREEN + "PyCalco [%i]: " % self.cmd_count + END 
        
        return line.lower() 
    
    def emptyline(self):
        pass
    
    def default(self,line):
        self.do_eval(line)
        
    def do_shell(self,line):
        self.do_assn(line)     
    
    def help_shell(self):
        print("A synomym or alias for ASSN command.")
        print("Usage: ! VAR = VAL")
    
    def do_eval(self, expression):
        try:
            print(eval(expression,GLOBALS))
        except Exception:
            print(RED + "SyntaxError" + END)
        
    def help_eval(self):
        print("Take an expression as arg and evaluate it.")
        print("Usage: eval EXPR")
        
        
    def do_assn(self, statement):
        if '=' in statement:
            l = statement.split('=')
            
            if len(l) == 2:
                l[0] = l[0].strip()
                l[1] = l[1].strip()
                pattern = r"(\D+\d*)+"
             
                if re.match(pattern,l[0]):
                    if re.match(r'\d+',l[1]):
                        GLOBALS[l[0]] = int(l[1])
                        print("%s = %d" % (l[0],int(l[1])))   
                    
        else:
            print(RED + "SyntaxError" + END)
        
    def help_assn(self):
        print("Assign a value to a variable.")
        print("Usage: assn VAR = VAL")
    
    
    def do_bye(self, arg):
        return True
    
    def help_bye(self):
        print("Terminate the session and return to the command interpreter.")
    
    
    def do_exit(self, arg):
        return self.do_bye(arg)
    
    def help_exit(self):
        print("A synonym or alias for BYE command.")

    
    def do_quit(self,arg):
        return self.do_bye(arg)
    
    def help_quit(self):
        print("A synonym or alias for BYE command.")

        
    def postloop(self):
        print("Bye, session terminated.")
        print("See you soon!")    
        
        
