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
    doc_header = "Documented available commands (type help <topic>):"
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
        print('Command for symbolic expression evaluation')

    def help_asym(self):
        print('Command for symbolic assignment')


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
   
    def do_acos(self, args):
        self.do_eval('acos(' + args + ')')

    def do_acosh(self, args):
        self.do_eval('acosh(' + args + ')')

    def do_asin(self, args):
        self.do_eval('asin(' + args + ')')

    def do_asinh(self, args):
        self.do_eval('asinh(' + args + ')')

    def do_atan(self, args):
        self.do_eval('atan(' + args + ')')

    def do_atan2(self, args):
        self.do_eval('atan2(' + args + ')')

    def do_atanh(self, args):
        self.do_eval('atanh(' + args + ')')

    def do_ceil(self, args):
        self.do_eval('ceil(' + args + ')')

    def do_copysign(self, args):
        self.do_eval('copysign(' + args + ')')

    def do_cos(self, args):
        self.do_eval('cos(' + args + ')')

    def do_sin(self, args):
        self.do_eval('sin(' + args + ')')

    def do_tan(self, args):
        self.do_eval('tan(' + args + ')')

    def do_cosh(self, args):
        self.do_eval('cosh(' + args + ')')

    def do_sinh(self, args):
        self.do_eval('sinh(' + args + ')')

    def do_tanh(self, args):
        self.do_eval('tanh(' + args + ')')

    def do_deg(self, args):
        self.do_eval('deg(' + args + ')')

    def do_rad(self, args):
        self.do_eval('rad(' + args + ')')

    def do_erf(self, args):
        self.do_eval('erf(' + args + ')')

    def do_erfc(self, args):
        self.do_eval('erfc(' + args + ')')

    def do_fabs(self, args):
        self.do_eval('fabs(' + args + ')')

    def do_exp(self, args):
        self.do_eval('exp(' + args + ')')

    def do_expm1(self, args):
        self.do_eval('expm1(' + args + ')')

    def do_complex(self, args):
        self.do_eval('complex(' + args + ')')

    def do_fac(self, args):
        self.do_eval('factorial(' + args + ')')

    def do_factorial(self, args):
        self.do_eval('factorial(' + args + ')')

    def do_floor(self, args):
        self.do_eval('floor(' + args + ')')

    def do_gamma(self, args):
        self.do_eval('gamma(' + args + ')')

    def do_gcd(self, args):
        self.do_eval('gcd(' + args + ')')

    def do_sqrt(self, args):
        self.do_eval('sqrt(' + args + ')')

    def do_rem(self, args):
        self.do_eval('remainder(' + args + ')')

    def do_mod(self, args):
        self.do_eval('mod(' + args + ')')

    def do_log(self, args):
        self.do_eval('log(' + args + ')')

    def do_log10(self, args):
        self.do_eval('log10(' + args + ')')

    def do_log1p(self, args):
        self.do_eval('log1p(' + args + ')')

    def do_log2(self, args):
        self.do_eval('acos(' + args + ')')

    def do_sum(self, args):
        self.do_eval('sum(' + args + ')')

    def do_prod(self, args):
        self.do_eval('prod(' + args + ')')

    def do_hex(self, args):
        self.do_eval('hex(' + args + ')')

    def do_oct(self, args):
        self.do_eval('oct(' + args + ')')

    def do_bin(self, args):
        self.do_eval('bin(' + args + ')')

    def do_pow(self, args):
        self.do_eval('pow(' + args + ')')

    def do_powmod(self, args):
        self.do_eval('powmod(' + args + ')')

    def do_round(self, args):
        self.do_eval('round(' + args + ')')

    def do_tau(self, args):
        self.do_eval('tau(' + args + ')')


    # Help methods for gobal functions
    
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

    def help_bin(self):
        help('bin')

    def help_ceil(self):
        help('math.ceil')

    def help_complex(self):
        help('math.complex')

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

    def help_fac(self):
        help('math.factorial')

    def help_factorial(self):
        help('math.factorial')

    def help_filter(self):
        help('math.filter')

    def help_floor(self):
        help('math.floor')

    def help_fmod(self):
        help('math.fmod')

    def help_frexp(self):
        help('math.frexp')

    def help_fsum(self):
        help('math.fsum')

    def help_gamma(self):
        help('math.gamma')

    def help_gcd(self):
        help('math.gcd')

    def help_hex(self):
        help('hex')

    def help_hypot(self):
        help('math.hypot')

    def help_log(self):
        help('math.log')

    def help_log10(self):
        help('math.log10')

    def help_log1p(self):
        help('math.log1p')

    def help_log2(self):
        help('math.log2')

    def help_max(self):
        help('math.max')

    def help_min(self):
        help('math.min')

    def help_mod(self):
        help('math.mod')

    def help_oct(self):
        help('oct')

    def help_pow(self):
        help('math.pow')

    def help_powmod(self):
        help('math.powmod')

    def help_prod(self):
        help('math.prod')

    def help_rem(self):
        help('math.remainder')

    def help_remainder(self):
        help('math.remainder')

    def help_round(self):
        help('math.round')

    def help_sin(self):
        help('math.sin')

    def help_sinh(self):
        help('math.sinh')

    def help_sqrt(self):
        help('math.sqrt')

    def help_sum(self):
        help('math.sum')

    def help_tan(self):
        help('math.tan')

    def help_tanh(self):
        help('math.tanh')

    def help_tau(self):
        help('math.tau')

    def help_trunc(self):
        help('math.trunc')


    def postloop(self):
        print("Bye, session terminated.")
        print("See you soon!")    
        
        
