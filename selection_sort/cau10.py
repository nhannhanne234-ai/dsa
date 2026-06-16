def selection_sort_exact_swaps(a: list) -> int:
    n = len(a)
    actual_swaps = 0
    for i in range(n - 1):
        min_idx = i
        for j in range(i + 1, n):
            if a[j] < a[min_idx]:
                min_idx = j
        if min_idx != i:
            a[i], a[min_idx] = a[min_idx], a[i]
            actual_swaps += 1
    return actual_swaps

a = [1, 2, 3]
swaps_count = selection_sort_exact_swaps(a)
print(f"mảng: {a} số lần swap thực tế: {swaps_count}")