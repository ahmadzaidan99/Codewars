def dig_pow(n, p):
    num=str(n)
    sum=0
    for i in range (len(num)):
        sum += int(num[i])**(p+i)
    return sum / n if (sum % n) == 0 else -1
