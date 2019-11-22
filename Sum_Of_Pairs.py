def sum_pairs(ints, s):
    comp = set()
    for i in ints:
        if s-i in comp:
            return [s-i,i]
        comp.add(i)                  
    return None
