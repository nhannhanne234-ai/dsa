def count_total_shifts_single_function(a):
    n = len(a)
    shifts = 0
    curr_size = 1
    while curr_size < n:
        for left in range(0, n, 2 * curr_size):
            mid = min(left + curr_size - 1, n - 1)
            right = min(left + 2 * curr_size - 1, n - 1)
            if mid < right:
                L = a[left : mid + 1]
                R = a[mid + 1 : right + 1]
                i = j = 0
                k = left
                while i < len(L) and j < len(R):
                    if L[i] <= R[j]:
                        a[k] = L[i]
                        i += 1
                    else:
                        a[k] = R[j]
                        shifts += (len(L) - i)
                        j += 1
                    k += 1
                while i < len(L):
                    a[k] = L[i]
                    i += 1
                    k += 1
                while j < len(R):
                    a[k] = R[j]
                    j += 1
                    k += 1
        curr_size = 2 * curr_size
    return shifts

a = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
total_shifts = count_total_shifts_single_function(a)
print(f"Tổng số lần shift: {total_shifts}")