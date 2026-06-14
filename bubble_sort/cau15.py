def object(a):
    n = len(a)
    for j in range(n-1):
        swapped = False
        for i in range(n-1-j):
            condition1 = a[i][1] < a[i+1][1]
            condition2 = (a[i][1] == a[i+1][1]) and (a[i][0] > a[i+1][0])
            if condition1 or condition2:
                a[i], a[i+1] = a[i+1], a[i]
                swapped = True
        if swapped == False:
            break
    return a

a = [('An',8), ('Ba',9), ('Cu',8), ('Linh',9), ('Anh',10), ('Nhan',10)]
print(object(a))