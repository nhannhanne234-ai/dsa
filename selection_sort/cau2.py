def selection_sort_ascending(a: list) -> list:
    n = len(a)
    for i in range(n - 1):
        min_idx = i
        for j in range(i + 1, n):
            if a[j] < a[min_idx]:
                min_idx = j
        a[i], a[min_idx] = a[min_idx], a[i]
    return a

print(selection_sort_ascending([5, 2, 4, 6, 1, 3]))