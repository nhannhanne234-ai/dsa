def selection_sort_descending(a: list) -> list:
    n = len(a)
    for i in range(n - 1):
        max_idx = i
        for j in range(i + 1, n):
            if a[j] > a[max_idx]:
                max_idx = j
        a[i], a[max_idx] = a[max_idx], a[i]
    return a

print(selection_sort_descending([5, 2, 4, 6, 1]))