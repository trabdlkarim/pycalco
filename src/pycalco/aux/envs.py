import builtins as blt
import math

import sympy

GREEN = '\033[92m'
RED = '\033[31m'
END = '\033[0m'
VER = '0.9.1'
_flag = False

GLOBS = {'__builtins__': {}, 'abs': blt.abs, 'all': blt.all, 'ans': None, 'any': blt.any, 
               'bin': blt.bin, 'mod': blt.divmod, 'hex': 'hex', 'max': blt.max, 'min': blt.min,
               'len': blt.len, 'oct': blt.oct, 'ord': blt.ord, 'powmod': blt.pow, 'round': blt.round, 
               'sorted': blt.sorted, 'sum': blt.sum, 'false': False, 'true': True, 'bool': blt.bool, 
               'complex': blt.complex, 'filter': blt.filter, 'float': blt.float, 'int': blt.int, 
               'map': blt.map, 'range': blt.range, 'zip': blt.zip,  
               'null': None, '_': None}
if not _flag:
    exec("from math import *", {"math": math}, GLOBS)
    _flag = True

SYM_ENV = { key: val for key, val in sympy.__dict__.items() if not key.startswith('__')}
