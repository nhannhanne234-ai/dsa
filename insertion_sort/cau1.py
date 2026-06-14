def insert(a, x):
    a.append(x)
    key = x
    j = len(a)-2
    while (j >= 0 and key<a[j]):
        a[j+1] = a[j]
        j-=1
    a[j+1] = key
    return a

a = [1, 3, 5, 7]
x = 4
print(insert(a, x))