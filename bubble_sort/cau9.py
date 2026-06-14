def bubble_sort_optimal(a):
    n = len(a)
    passes = 0
    for j in range(n-1):
        swapped = False
        for i in range(n-1-j):
            if a[i] > a[i+1]:
                a[i], a[i+1] = a[i+1], a[i]
                swapped = True
        passes += 1
        if swapped == False:
            break
    return passes

a = [1, 2, 3, 4]
print(bubble_sort_optimal(a))