def persistence(n):
    arr = [int(x) for x in str(n)]
    count = 0
    while(len(arr)!=1):
        result=1
        count += 1
        for x in arr:
            result *= x
        arr = [int(x) for x in str(result)]
    return count
