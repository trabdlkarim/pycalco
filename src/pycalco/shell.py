import sys
import builtins as blt

import math
import cmd
import re

import click


GREEN = '\033[92m'
RED = '\033[31m'
END = '\033[0m'

__version__ = "0.9.1"

__globals__ = {'__builtins__': {}, 'abs': blt.abs, 'all': blt.all, 'ans': None, 'any': blt.any, 
               'bin': blt.bin, 'mod': blt.divmod, 'hex': 'hex', 'max': blt.max, 'min': blt.min,
               'len': blt.len, 'oct': blt.oct, 'ord': blt.ord, 'powmod': blt.pow, 'round': blt.round, 
               'sorted': blt.sorted, 'sum': blt.sum, 'false': False, 'true': True, 'bool': blt.bool, 
               'complex': blt.complex, 'filter': blt.filter, 'float': blt.float, 'int': blt.int, 
               'map': blt.map, 'range': blt.range, 'zip': blt.zip, 
         
               'acos': math.acos, 'acosh': math.acosh, 'asin': math.asin, 'asinh': math.asinh,
               'atan': math.atan, 'atan2': math.atan2, 'atanh': math.atanh, 'ceil': math.ceil,
               'copysign': math.copysign, 'cos': math.cos, 'cosh': math.cosh, 
               'deg': math.degrees, 'e': math.e, 'erf': math.erf, 'erfc': math.erfc,
               'exp': math.exp, 'expm1': math.expm1, 'fabs': math.fabs, 'fac': math.factorial,
               'floor': math.floor, 'fmod': math.fmod, 'frexp': math.frexp, 'fsum': math.fsum,
               'gamma': math.gamma, 'gcd': math.gcd, 'hypot': math.hypot, 'inf': math.inf,
               'isclose': math.isclose, 'isfinite': math.isfinite, 'isinf': math.isinf,
               'isnan': math.isnan, 'ldexp': math.ldexp, 'lgamma': math.lgamma, 'log': math.log,
               'log10': math.log10, 'log1p': math.log1p, 'log2': math.log2, 'modf': math.modf,
               'nan': math.nan, 'pi': math.pi, 'pow': math.pow, 'rad': math.radians, 
               'rem': math.remainder, 'sin': math.sin, 'sinh': math.sinh, 'sqrt': math.sqrt,
               'tan': math.tan, 'tanh': math.tanh, 'tau': math.tau, 'trunc': math.trunc,      
               'null': None, '_': None}
         
__locals__ = {}

class PyCalcoShell(cmd.Cmd):
    intro = "Welcome to PyCalco shell!\n"
    intro += 'Python ' + sys.version + '\n'
    intro += "Type 'copyright', 'credits' or 'license' for more information.\n"
    intro += "PyCalco " + __version__ + " -- A Powerful Arithmetic Expressions Evaluator.\n"
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
        
        if line:
            return line.replace(line.split()[0], line.split()[0].lower())
        
        else: return line
    
    def emptyline(self):
        pass
    
    def default(self,line):
        self.do_eval(line)
        
    def do_copyright(self, line):
        """A command for printing project copyright notice."""
        print("Copyright (c) 2021 Toure A. Karim and Contributors.")
        print("All Rights Reserved.")
    
    
    def do_credits(self, line):
        """A command for printing a list of contributors."""
        print("Thanks to  all the contributors for supporting PyCalco development.")
        print("See 'gh.trabdlkarim.com/pycalco' for more information.")
   
    def do_license(self, line):
        """A command for printing the project license."""
        print('This is an open source project, and its code is being actively developed in the open on GitHub.') 
        print("PyCalco is under the BSD 3-Clause Revised license.")
        print("For more info about the license see 'https.gh.trabdlkarim/pycalco/license'.")
    
  
    def do_shell(self,line):
        """A bang shortcut for assn command (i.e,!NAME = EXPR is same as assn NAME = EXPR)."""
        self.do_assn(line)     
 
    
    def do_eval(self, expression):
        try:
            if not expression:
                raise SyntaxError("invalid syntax for eval command (expression is missing).")
            
            code_obj = compile(expression,'<string>','eval')
            
            for name in code_obj.co_names:
                if name not in __globals__ and name not in __locals__:
                    raise NameError('name ' +"'" + name +"'" + ' is not defined' )

            print(eval(expression,__globals__,__locals__))

        except Exception as err:
            print(RED + "error: " + END + str(err) )
        
    def help_eval(self):
        print("Evaluate given the expression.")
        print("usage: eval EXPR")
        
        
    def do_assn(self, statement):
        equal = None
        for i in range(len(statement)):
            if statement[i] == '=':
                equal = i
                break
        if equal:
            var = statement[:equal].strip()
            expr = statement[equal+1:].strip()
            try:
                code_obj = compile(expr,'<string>','eval')

                for name in code_obj.co_names:
                    if name not in __globals__ and name not in __locals__:
                        raise NameError('name '+ "'" + name + "'"  + ' is not defined')
                
                expr = eval(expr,__globals__)
                exec(var + ' = ' + str(expr),{}) 
                __locals__[var]= expr
                print("%s = %s" % (var,expr))   
            
            except Exception as err:
                print(RED+ "error: " + END + str(err))
        else:
            print(RED + "error: " + END + "invalid syntax for assn command (type '?assn' for help).")
        
    def help_assn(self):
        print("Assign a value to a variable.")
        print("usage: assn VAR = EXPR")
   
    
    def do_globals(self, args):
        """A command for listing all available global names."""
        names = [name for name in __globals__.keys() if not name.startswith('__')]
        print(sorted(names))
    
    def do_locals(self, args):
        """A command for listing all available locals names."""
        print(__locals__)
        
    def do_bye(self, args):
        """A synonym or alias for EXIT command."""
        return True
    
    
    def do_exit(self, arg):
        """Terminate the session and return to the command interpreter."""
        return self.do_bye(arg)
    
    
    def do_quit(self,arg):
        """A synonym or alias for EXIT command."""
        return self.do_bye(arg)
   
    
    # Help methods for gobals
    
    def help_acos(self):
        help('math.acos')

    def help_acosh(self):
        help('math.acosh') 
    
    def help_asin(self):
        help('math.asin')

    def help_asinh(self):
        help('math.asinh')
    
    def help_atan(eself):
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

    def postloop(self):
        print("Bye, session terminated.")
        print("See you soon!")    
        
        
