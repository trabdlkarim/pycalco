
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
                
                expr = eval(expr,__globals__,__locals__)
                
                exec(var + ' = ' + str(expr),{'__builtins__':{}},__locals__) 
                
                if var not in __globals__:
                    print("%s = %s" % (var,expr))   
                
                else:
                    raise NameError("can't reassign global " + "'" + var + "' (" + str(type(__globals__[var])) + ")")

            except Exception as err:
                print(RED+ "error: " + END + str(err))
        else:
            print(RED + "error: " + END + "invalid syntax for assn command (type '?assn' for help)")
        
