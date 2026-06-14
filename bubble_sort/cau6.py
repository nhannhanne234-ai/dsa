def cr_in_one_turn(a):
    n = len(a)
    for i in range(n-1):
        if a[i] > a[i+1]:
            a[i], a[i+1] = a[i+1], a[i]
    return a[-1]

a = [7, 2, 7, 1, 3]
result = cr_in_one_turn(a)
print(result)