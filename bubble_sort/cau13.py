def stability(a):
    n = len(a)
    for j in range(n-1):
        swapped = False
        for i in range(n-1-j):
            condition1 = a[i][0] > a[i+1][0]                                    # so sánh ở index 0 cái nào lớn hơn (number)
            condition2 = (a[i][0] == a[i+1][0]) and (a[i][1] > a[i+1][1])       # hai số bằng nhau thì qua index 1 so sánh chữ (letter)
            if condition1 or condition2:
                a[i], a[i+1] = a[i+1], a[i]
                swapped = True
        if swapped == False:
            break
    return a

a = [(2,'a'),(1,'b'),(2,'c')]
print(stability(a))