def fl_k(a, k):
    n = len(a)
    for j in range(k):
        for i in range(n-1):
            if a[i] > a[i+1]:
                a[i], a[i+1] = a[i+1], a[i]
                
    is_sorted = True
    for j in range(n-1):
        if a[j] > a[j+1]:
            is_sorted = False
            break
    return is_sorted

a = [3, 2, 1]
k = 2
result = fl_k(a, k)
print(result)