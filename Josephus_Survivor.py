def josephus_survivor(n,k):
    list = [] 
    m=1
    delete=0
    while(m < n+1 ): 
        list.append(m) 
        m += 1
    while(len(list)!=1):
        delete+=k-1
        while (delete>(len(list)-1)):
            delete=abs(len(list)-delete)
        list.pop(delete)
    return list[0]
