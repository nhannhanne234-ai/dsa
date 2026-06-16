def double_ended_selection_sort(a):
    n = len(a)
    # Giảm số vòng lặp còn một nửa (chỉ chạy đến n // 2)
    for i in range(n // 2):
        min_idx = i
        max_idx = i
        for j in range(i, n - i):
            if a[j] < a[min_idx]:
                min_idx = j
            if a[j] > a[max_idx]:
                max_idx = j
        a[i], a[min_idx] = a[min_idx], a[i]
        if max_idx == i:
            max_idx = min_idx
        a[n - 1 - i], a[max_idx] = a[max_idx], a[n - 1 - i]
        
    return a

a = [5, 1, 4, 2, 8]
print(double_ended_selection_sort(a))