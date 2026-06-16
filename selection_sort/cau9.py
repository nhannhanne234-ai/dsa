def double_selection_sort(a: list) -> list:
    n = len(a)
    left = 0
    right = n - 1
    while left < right:
        min_idx = left
        max_idx = left
        for i in range(left + 1, right + 1):
            if a[i] < a[min_idx]:
                min_idx = i
            if a[i] > a[max_idx]:
                max_idx = i
        a[left], a[min_idx] = a[min_idx], a[left]
        if max_idx == left:
            max_idx = min_idx
        a[right], a[max_idx] = a[max_idx], a[right]
        left += 1
        right -= 1
    return a

print(double_selection_sort([5, 1, 4, 2, 8]))