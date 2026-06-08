def fl_k(a, k):
    n = len(a)
    for j in range(k):
        for i in range(n-1):
            if a[i] > a[i+1]:
                a[i], a[i+1] = a[i+1], a[i]
    if j == k - 1:
        return True
    return False

a = [3, 2, 1]
k = 2
result = fl_k(a, k)
print(result)