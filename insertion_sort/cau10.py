def counter_number(a):
    n = len(a)
    count = 0
    for i in range(1,n):
        key = a[i]
        j = i - 1
        while j >= 0 and key < a[j]:
            a[j+1] = a[j]
            count += 1
            j -= 1
        a[j+1] = key
    return count

a = [2, 4, 1, 3]
result = counter_number(a)
print(f"{result} nghịch thế = {result} shift")