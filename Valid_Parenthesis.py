def valid_parentheses(string):
    list=[]
    for x in string:
        if x == '(':
            list.append(x)
        if x == ')':
            try:
                list.pop()
            except:
                return False
              
    if len(list)==0:return True 
    else:return False
