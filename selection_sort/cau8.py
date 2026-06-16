def find_min_index_in_range(a: list, i: int) -> int:
    min_idx = i
    for j in range(i + 1, len(a)):
        if a[j] < a[min_idx]:
            min_idx = j
    return min_idx

print(find_min_index_in_range([9, 3, 7, 1, 5], i=1))