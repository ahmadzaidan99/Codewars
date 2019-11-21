def delete_nth(order,max_e):
    counter= {}
    newlist = []
    for i in order:
        if i not in counter:
            counter[i]=0
        else:
            counter[i] += 1
        if counter[i]<max_e:
            newlist.append(i)
    return newlist
