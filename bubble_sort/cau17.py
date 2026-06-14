def bubble_sort_fl_k(a, k):
    n = len(a)
    for j in range(k):
        for i in range(n-1-j):
            if a[i] > a[i+1]:
                a[i], a[i+1] = a[i+1], a[i]
    return a

a = [3, 1, 4, 1, 5]
k = 2
result = bubble_sort_fl_k(a, k)
print(result)