def riel_swap(a):
    n = len(a)
    pass_count = 0
    for j in range(n):
        swapped = False
        for i in range(n-j-1):
            if a[i] > a[i+1]:
                a[i], a[i+1] = a[i+1], a[i]
                swapped = True
        pass_count += 1
        if not swapped:
            break
            
    return pass_count

a = list(range(1, 1001))

for i in range(0, len(a) - 3, 3):
    a[i], a[i+2] = a[i+2], a[i]

print(f"Số lượt quét thực tế: {riel_swap(a)} lượt")