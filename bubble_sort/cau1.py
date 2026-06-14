def one_pass(a):
    n = len(a)
    for i in range(n-1):
        if a[i] > a[i+1]:
            a[i], a[i+1] = a[i+1], a[i]
    return a

a = [5, 1, 4, 2, 8]
result = one_pass(a)
print(result)