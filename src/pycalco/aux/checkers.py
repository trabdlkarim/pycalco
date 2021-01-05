def assn_checker(stmt, globs, locs):
    eq_sign = None
    for i in range(len(stmt)):
        if stmt[i] == '=':
            eq_sign = i
            break
    if eq_sign:
        var = stmt[:eq_sign].strip()
        expr = stmt[eq_sign+1:].strip()
       
        code_obj = compile(expr,'<string>','eval')

        for name in code_obj.co_names:
            if name not in globs and name not in locs:
                raise NameError('name '+ "'" + name + "'"  + ' is not defined')
                
        expr = eval(expr, globs, locs)
        exec(var + ' = ' + str(expr),{'__builtins__':{}}, locs) 
                
        if var not in globs:
            return "%s = %s" % (var, expr)
        else:
            raise NameError("can't reassign global " + "'" + var + "' (" + str(type(globs[var])) + ")")
    else:
        raise SyntaxError("invalid syntax for assignment (type '?assn' for help)")
        

 
def expr_checker(expression, globs, locs):
        try:
            if not expression:
                raise SyntaxError("invalid syntax for eval command (expression is missing).")
            
            code_obj = compile(expression,'<string>','eval')
            
            for name in code_obj.co_names:
                if name not in __globals__ and name not in __locals__:
                    raise NameError('name ' +"'" + name +"'" + ' is not defined' )

            result = eval(expression,__globals__,__locals__)
            print(result)
            __globals__['ans'] = __globals__['_'] = result
        
        except Exception as err:
            print(RED + "error: " + END + str(err) )
