def stable_selection_sort(a: list) -> list:
    n = len(a)
    for i in range(n - 1):
        min_idx = i
        for j in range(i + 1, n):
            if a[j][0] < a[min_idx][0]:
                min_idx = j
        key = a[min_idx]
        while min_idx > i:
            a[min_idx] = a[min_idx - 1]
            min_idx -= 1
        a[i] = key
    return a

a = [(2, 'a'), (2, 'b'), (1, 'c')]
print(stable_selection_sort(a))