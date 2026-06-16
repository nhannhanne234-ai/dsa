def selection_sort_count_comps(a: list) -> int:
    n = len(a)
    comp_count = 0
    for i in range(n - 1):
        min_idx = i
        for j in range(i + 1, n):
            comp_count += 1
            if a[j] < a[min_idx]:
                min_idx = j
        a[i], a[min_idx] = a[min_idx], a[i]
    return comp_count

a = [5, 4, 3, 2, 1]
comps = selection_sort_count_comps(a)
print(f"số lần so sánh với n=5 là: {comps}")