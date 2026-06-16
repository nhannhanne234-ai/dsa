def count_comparisons_selection_sort(arr):
    n = len(arr)
    comparisons = 0
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            comparisons += 1
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return comparisons

n = 5
print("mảng sắp xếp [1,2,3,4,5]:", count_comparisons_selection_sort([1, 2, 3, 4, 5]), "lần so sánh.")
print("mảng ngược [5,4,3,2,1]:", count_comparisons_selection_sort([5, 4, 3, 2, 1]), "lần so sánh.")
print("mảng random [3,5,1,4,2]:", count_comparisons_selection_sort([3, 5, 1, 4, 2]), "lần so sánh.")