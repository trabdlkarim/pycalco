import sys
import cmd

import pycalco
from pycalco.aux.envs import *
from pycalco.aux.checkers import *

GREEN = '\033[92m'
RED = '\033[31m'
END = '\033[0m'

__globals__ = GLOBS   
__locals__ = {}
__sympy_env__ = SYM_ENV

class PyCalcoShell(cmd.Cmd):
    intro = "Welcome to PyCalco shell!\n"
    intro += 'Python ' + sys.version + '\n'
    intro += "Type 'copyright', 'credits' or 'license' for more information.\n"
    intro += "PyCalco " + pycalco.version + " -- A Powerful Arithmetic Expressions Evaluator.\n"
    intro += "Type 'help' or '?' for help.\n"
    intro += "Type 'bye', 'exit' or 'quit' for ending this session.\n\n"
    
    prompt = GREEN + "PyCalco [%i]: " + END
    doc_header = "Documented avaible commands (type help <topic>):"
    misc_header = "Globals and miscellaneous help topics:"    
    
    def preloop(self):
        self.cmd_count = 1
        PyCalcoShell.prompt = PyCalcoShell.prompt % self.cmd_count 
    
    def precmd(self,line):
        self.cmd_count += 1
        PyCalcoShell.prompt = GREEN + "PyCalco [%i]: " % self.cmd_count + END 
        return line

    def emptyline(self):
        pass
    
    def default(self,line):
        if '=' in line:
            self.do_assn(line)
        else:
            self.do_eval(line)
        
    def do_copyright(self, args):
        """A command for printing project copyright notice."""
        if not args:
            print("Copyright (c) 2021 Toure A. Karim and Contributors.")
            print("All Rights Reserved.")
        else:
            print(RED + "error: " + END + "too many args (takes no arg but one was given)")
    
    def do_credits(self, args):
        """A command for printing a list of contributors."""
        if not args:
            print("Thanks to  all the contributors for supporting PyCalco development.")
            print("See 'gh.trabdlkarim.com/pycalco' for more information.")
        else:   
            print(RED + "error: " + END + "too many args (takes no arg but one was given)")
    
    def do_license(self, args):
        """A command for printing the project license."""
        if not args:
            print('This is an open source project, and its code is being actively developed in the open on GitHub.') 
            print("PyCalco is under the BSD 3-Clause Revised license.")
            print("For more info about the license see 'https.gh.trabdlkarim/pycalco/license'.")
        else:
            print(RED + "error: " + END + "too many args (takes no arg but one was given)")
    
    def do_init(self, args):
        """Initialize shell local environment."""
        if not args:
            global __locals__
            __locals__ = {}
            print("Local environment successfully initialized.")
        else:
            print(RED + "error: " + END + "too many args (takes no arg but one was given)")
    
    def do_shell(self, args):
        """A bang shortcut for symbolic assignment command (i.e,!NAME = EXPR is same as asym NAME = EXPR)."""
        self.do_asym(args)     
 
    
    def do_eval(self, expression):
        try:
            result = expr_checker(expression, __globals__, __locals__)
            print(result)
            __globals__['ans'] = __globals__['_'] = result
        except Exception as err:
            print(RED + "error: " + END + str(err) )
        
    def help_eval(self):
        print("Evaluate given the expression.")
        print("usage: eval EXPR")
        
        
    def do_assn(self, stmt):
        try:  
            result = assn_checker(stmt, __globals__, __locals__)
            print(result)  
        except Exception as err:
            print(RED+ "error: " + END + str(err))
        
    def help_assn(self):
        print("Assign a value to a variable.")
        print("usage: assn VAR = EXPR")


    def do_sym(self, args):
        try:
            result =  expr_checker(args, __sympy_env__, __locals__)
            print(result)
            __globals__['ans'] = __globals__['_'] = result
        except Exception as err:
            print(RED + "error: " + END + str(err))
    
    def do_asym(self,args):
        try:
            result =  assn_checker(args, __sympy_env__, __locals__)
            print(result)
        except Exception as err:
            print(RED + "error: " + END + str(err))

    def help_sym(self):
        print('Command for symbolic computation')


    def do_globals(self, args):
        """A command for listing all available global names."""
        if not args:
            names = [name for name in __globals__.keys() if not name.startswith('__')]
            print(sorted(names))
      
        else:
            print(RED + "error: " + END + "too many args (takes no arg but one was given)")

    def do_locals(self, args):
        """A command for listing all available locals names."""
        if not args:
            print(__locals__)
            
        else:
            print(RED + "error: " + END + "too many args (takes no arg but one was given)")

    def do_bye(self, args):
        """A synonym or alias for exit command."""
        if not args:
            return True
            
        else:
            print(RED + "error: " + END + "too many args (takes no arg but one was given)")
            return False

    def do_exit(self, args):
        """Terminate the session and exit the command interpreter."""
        return self.do_bye(args)
    
    
    def do_quit(self,args):
        """A synonym or alias for exit command."""
        return self.do_bye(args)
   
    
    # Help methods for gobals
    
    def help_acos(self):
        help('math.acos')

    def help_acosh(self):
        help('math.acosh') 
    
    def help_asin(self):
        help('math.asin')

    def help_asinh(self):
        help('math.asinh')
    
    def help_atan(self):
        help('math.atan')
    
    def help_atan2(self):
        help('math.atan2')
    
    def help_atanh(self):
        help('math.atanh')
    
    def help_ceil(self):
        help('math.ceil')

    def help_copysign(self):
        help('math.copysign')

    def help_cos(self):
        help('math.cos')

    def help_cosh(self):
        help('math.cosh')

    def help_deg(self):
        help('math.degrees')
 
    def help_rad(self):
        help('math.radians')
   
    def help_e(self):
        help('math.e')
     
    def help_erf(self):
        help('math.erf')

    def help_erfc(self):
        help('math.erfc')

    def help_exp(self):
        help('math.exp')
 
    def help_expm1(self):
        help('math.expm1')

    def help_fabs(self):
        help('math.fabs')

    def postloop(self):
        print("Bye, session terminated.")
        print("See you soon!")    
        
        
