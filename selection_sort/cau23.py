def analyze_selection_sort(a):
    n = len(a)
    swaps = 0
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if a[j] < a[min_idx]:
                min_idx = j
        if min_idx != i:
            a[i], a[min_idx] = a[min_idx], a[i]
            swaps += 1
    return swaps

print("đã sắp xếp [1, 2, 3, 4, 5] (Best Case):", analyze_selection_sort([1, 2, 3, 4, 5]), "lần swap.")
print("ngẫu nhiên  [3, 5, 1, 4, 2] (Average Case):", analyze_selection_sort([3, 5, 1, 4, 2]), "lần swap.")
print("sắp xếp ngược [5, 4, 3, 2, 1] (Worst Case):", analyze_selection_sort([5, 4, 3, 2, 1]), "lần swap.")