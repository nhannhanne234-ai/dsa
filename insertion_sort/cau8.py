def base_insert(a,k):
    for i in range(1,k+1):
        key = a[i]
        j=i-1
        while (j>=0 and key<a[j]):
            a[j+1] = a[j]
            j-=1
        a[j+1]=key
    return a

a = [4, 3, 2, 1]
k = 1
result = base_insert(a, k)
print(result)