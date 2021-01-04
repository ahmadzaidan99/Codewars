def matrix_mult(a, b):
    mul = []
    for i in range (len(a)):
        row=[]
        for j in range (len(a)):
            x=0
            for k in range(len(a)):
                x+=a[i][k] * b[k][j]
            row.append(x)
        mul.append(row)
    return mul
