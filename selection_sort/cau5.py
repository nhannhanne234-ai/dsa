def selection_sort_count_swaps(a: list) -> int:
    n = len(a)
    swap_count = 0
    for i in range(n - 1):
        min_idx = i
        for j in range(i + 1, n):
            if a[j] < a[min_idx]:
                min_idx = j
        a[i], a[min_idx] = a[min_idx], a[i]
        swap_count += 1
    return swap_count

a = [3, 2, 1]
swaps = selection_sort_count_swaps(a)
print(f"mảng sau sắp xếp: {a} số lần swap: {swaps}")