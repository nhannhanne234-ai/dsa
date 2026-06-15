def insertion_sort_k_bounded(a):
    n = len(a)
    shifts = 0
    for i in range(1, n):
        key = a[i]
        j = i - 1
        while j >= 0 and key < a[j]:
            a[j + 1] = a[j]
            shifts += 1
            j -= 1
        a[j + 1] = key
    return a, shifts

mang_lech_k = [3, 2, 1, 5, 4, 6] 
sorted_arr, total_shifts = insertion_sort_k_bounded(mang_lech_k)

print(f"mảng sau xếp: {sorted_arr}")
print(f"tổng shift: {total_shifts}")
print(f"thực tế số shiftt {total_shifts} luôn <= n*k.")