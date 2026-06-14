def string_length(a):
    n = len(a)
    for j in range(n-1):
        swapped = False
        for i in range(n-1-j):
            if len(a[i]) > len(a[i+1]):
                a[i], a[i+1] = a[i+1], a[i]
                swapped = True
        if swapped == False:
            break
    return a

a = ['abc', 'a', 'ab']
print(string_length(a))