def bubble_sort(a):
    n = len(a)
    count = 0
    for j in range(n-1):
        for i in range(n-1):
            count += 1
            if a[i] > a[i+1]:
                a[i], a[i+1] = a[i+1], a[i]
    return count

a = [1, 2, 3]
result = bubble_sort(a)
print(f"Số lần đếm là: {result}")