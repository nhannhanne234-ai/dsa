def selection_sort_absolute_pure(a: list) -> list:
    n = len(a)
    for i in range(n - 1):
        min_idx = i
        for j in range(i + 1, n):
            val_j = a[j]
            if val_j < 0:
                val_j = -val_j
            val_min = a[min_idx]
            if val_min < 0:
                val_min = -val_min
            if val_j < val_min:
                min_idx = j
        a[i], a[min_idx] = a[min_idx], a[i]
    return a

a = [-3, 1, -2, 2]
print(selection_sort_absolute_pure(a))