def analyze_insertion_sort(a):
    arr = a.copy()
    n = len(arr)
    comparisons = 0
    shifts = 0
    for i in range(1, n):
        key = arr[i]
        j = i - 1
        while j >= 0:
            comparisons += 1
            if key < arr[j]:
                arr[j + 1] = arr[j]
                shifts += 1
                j -= 1
            else:
                break
        else:
            pass
        arr[j + 1] = key
    return comparisons, shifts

n = 5
best_in    = [1, 2, 3, 4, 5]
average_in = [3, 1, 5, 2, 4]
worst_in   = [5, 4, 3, 2, 1]

c_best, s_best = analyze_insertion_sort(best_in)
c_avg, s_avg   = analyze_insertion_sort(average_in)
c_worst, s_worst = analyze_insertion_sort(worst_in)

print(f"Kích thước mảng n = {n}")
print(f"1. Đã sắp xếp (Best): {c_best} so sánh, {s_best} shifts")
print(f"2. Ngẫu nhiên (Average): {c_avg} so sánh, {s_avg} shifts")
print(f"3. Sắp xếp ngược (Worst): {c_worst} so sánh, {s_worst} shifts")