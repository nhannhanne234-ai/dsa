def sentinel_search(a, x):
    n = len(a)
    if n == 0:
        return -1
        
    last_element = a[n - 1]
    a[n - 1] = x
    
    i = 0
    while a[i] != x:
        i += 1
        
    a[n - 1] = last_element
    
    if i < n - 1 or a[n - 1] == x:
        return i
    return -1

a17 = [7, 3, 9, 12, 5, 8, 1]
print(sentinel_search(a17, 12))