def base_insert(a):
    n = len(a)
    for i in range(1,n):
        key = a[i]
        j=i-1
        while j>=0:
            condition1 = (key[1] > a[j][1]) 
            condition2 = (key[1] == a[j][1]) and (key[0] < a[j][0])
            if condition1 or condition2:
                a[j+1] = a[j]
                j-=1
            else:
                break
        a[j+1]=key
    return a

a = [('An',8),('Ba',9),('Cu',8)]
result = base_insert(a)
print(result)