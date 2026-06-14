def d_insert(a):
    n = len(a)
    for i in range(1,n):
        key = a[i]
        j = i-1
        while (j>=0 and key<a[j]):
            a[j+1] = a[j]
            j-=1
        a[j+1]=key
        print(a)

a = [3, 1, 2]
result = d_insert(a)
print(result)