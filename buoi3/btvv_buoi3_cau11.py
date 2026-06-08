def absolute_cure(a):
    n = len(a)
    for j in range(n-1):
        swapped = False
        for i in range(n-1-j):
            condition1 = a[i]**2 > a[i+1]**2                            # trị tuyệt đối trước lớn hơn sau
            condition2 = (a[i]**2 == a[i+1]**2) and (a[i] > a[i+1])     # hai trị tuyệt đối bằng nhau nhưng giá trị trước lớn hơn sau
            if condition1 or condition2: 
                a[i], a[i + 1] = a[i + 1], a[i]
                swapped = True
        if swapped == False:
            break
    return a

a = [-3, 1, 2, -2]
print(absolute_cure(a))