def len_string(a):
    n = len(a)
    for i in range(1,n):
        key = a[i]
        j=i-1
        while (j>=0 and len(key) < len(a[j])):
            a[j+1] = a[j]
            j-=1
        a[j+1]=key
    return a

a = ['abc', 'a', 'ab']
result = len_string(a)
print(result)