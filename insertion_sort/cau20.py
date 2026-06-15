def shell_sort(a, gap_sequence):
    n = len(a)
    shift_count = 0
    for gap in gap_sequence:
        for i in range(gap, n):
            key = a[i]
            j = i
            while j >= gap and a[j - gap] > key:
                a[j] = a[j - gap]
                shift_count += 1
                j -= gap
            a[j] = key
    return a, shift_count


def sort_gap_shell(n):
    gaps = []
    gap = n // 2
    while gap > 0:
        gaps.append(gap)
        gap //= 2
    return gaps
def sort_gap_knuth(n):
    gaps = []
    h = 1
    while h < n:
        gaps.append(h)
        h = 3 * h + 1
    return gaps[::-1]

a1 = [9, 1, 5, 8, 3, 7, 4, 2]
a2 = a1.copy()
n = len(a1)

gap_shell = sort_gap_shell(n)
shifts_shell = shell_sort(a1, gap_shell)

gap_knuth = sort_gap_knuth(n)
shifts_knuth = shell_sort(a2, gap_knuth)

print(f"dãy gap (n/2): {gap_shell}, số lần shift: {shifts_shell}")
print(f"dãy gap Knuth: {gap_knuth}, số lần shift: {shifts_knuth}")