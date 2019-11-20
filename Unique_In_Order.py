def unique_in_order(iterable):
    list=[]
    for i in iterable:
        if len(list)<1 or not i == list[len(list) - 1]:#if the list is empty or if the element doesn't match the element before it append
            list.append(i)
    return list
