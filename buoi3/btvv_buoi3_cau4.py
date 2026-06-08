def bubble_sort(a):
    n = len(a)
    swap = 0
    for j in range(n-1):
        for i in range(n-1):
            if a[i] > a[i+1]:
                a[i], a[i+1] = a[i+1], a[i]
                swap += 1
    return swap

a = [3, 2, 1]
result = bubble_sort(a)
print(f"Số lần hoán đổi là: {result}")