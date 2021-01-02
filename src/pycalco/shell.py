import sys
import cmd
import click

GREEN = '\033[92m'
END = '\033[0m'
VERSION = "0.9.0"

class PyCalcoShell(cmd.Cmd):
    intro = "\nWelcome to PyCalco shell.\n"
    intro += "Type 'help' or '?' to list all available commands.\n"
    intro += "PyCalco " + VERSION + " --A Powerful Python Arithmetic Calculator\n\n"
    prompt = GREEN + "PyCalco [%i]: " + END
    
    def preloop(self):
        self.cmd_count = 1
        PyCalcoShell.prompt = PyCalcoShell.prompt % self.cmd_count 
    
    def precmd(self,line):
        self.cmd_count += 1
        PyCalcoShell.prompt = GREEN + "PyCalco [%i]: " % self.cmd_count + END 
        
        return line.lower() 
        
    def do_eval(self, expression):
        pass
        
    def help_eval(self):
        print("Take an expression as arg and evaluate it.")
        
        
    def do_assn(self, statment):
        pass
    
    def help_assn(self):
        print("Assign a value to a variable")
    
    
    def do_bye(self,arg):
        return True
    
    def help_bye(self):
        print("Terminate the session and return to the command interpreter.")
    
    
    def do_exit(self, arg):
        return self.do_bye(arg)
    
    def help_exit(self):
        print("A synonym or alias for bye command.")

    
    def do_quit(self,arg):
        return self.do_bye(arg)
    
    def help_quit(self):
        print("A synonym or alias for bye command.")

        
    def postloop(self):
        print("Bye, session terminated.")
        print("See you soon!")    
        
        
