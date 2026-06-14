def key_value(a):
    n = len(a)
    for j in range(n-1):
        swapped = False
        for i in range(n-1-j):
            if a[i][0] > a[i+1][0]:
                a[i], a[i+1] = a[i+1], a[i]
                swapped = True
        if swapped == False:
            break
    return a

data_test = [(2, 'X'), (1, 'Y'), (2, 'Z'), (1, 'W')]
result = key_value(data_test)
print(result)