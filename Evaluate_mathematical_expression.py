def calc(expression):
    ex = list(expression.replace(' ', ''))

    def peek():
        return ex[0] if ex else ''
    
    def get():
        return ex.pop(0)
    
    def number():
        result = get()
        while peek() >= '0' and peek() <= '9' or peek() == '.':
            result += get()        
        return float(result)
    
    def factor():
        if peek() >= '0' and peek() <= '9': 
            return number()
        elif peek() == '(':
            get() # '('
            result = expression()
            get() # ')'
            return result
        elif peek() == '-': 
            get()
            return -factor()        
        return 0 # error
    
    def term():
        result = factor()
        while peek() == '*' or peek() == '/':
            if get() == '*': 
                result *= factor()
            else:
                result /= factor()   
        return result
    
    def expression():
        result = term()
        while peek() == '+' or peek() == '-':
            if get() == '+':
                result += term()
            else:
                result -= term()                    
        return result

    return expression()
