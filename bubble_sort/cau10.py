def early_exit(a):
    n = len(a)
    if n <= 1:
        return 0
    
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

a = [2, 1, 3, 4]
print(early_exit(a))