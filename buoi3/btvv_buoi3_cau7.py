def bubble_sort_letter(a):
    n = len(a)
    for j in range(n-1):
        for i in range(n-1):
            if a[i] > a[i+1]:
                a[i], a[i+1] = a[i+1], a[i]
    return a

a = ['d', 'a', 'c', 'b']
result = bubble_sort_letter(a)
print(result)