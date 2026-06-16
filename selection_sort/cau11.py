def demonstrate_instability():
    a = [(2, 'a'), (2, 'b'), (1, 'c')]
    n = len(a)
    for i in range(n - 1):
        min_idx = i
        for j in range(i + 1, n):
            if a[j][0] < a[min_idx][0]:
                min_idx = j
        a[i], a[min_idx] = a[min_idx], a[i]
    return a

print(demonstrate_instability())