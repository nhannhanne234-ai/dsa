def early_exit(a):
    n = len(a)
    pass_count = 0
    for i in range(n):
        swapped = False
        for j in range(0, n-i-1):
            if a[j] > a[j+1]:
                a[j], a[j+1] = a[j+1], a[j]
                swapped = True
        pass_count += 1
        if swapped == False:
            break
    return pass_count

a = [1, 2, 3, 5, 4]
result = early_exit(a)
print(f"{result} lượt")