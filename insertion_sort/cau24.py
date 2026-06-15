import random
def bubble_sort(arr):
    a = arr.copy()
    n = len(a)
    comparisons = 0
    swaps = 0
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            comparisons += 1
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
                swaps += 1
                swapped = True
        if not swapped:
            break
    return comparisons, swaps

def selection_sort(arr):
    a = arr.copy()
    n = len(a)
    comparisons = 0
    swaps = 0
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            comparisons += 1
            if a[j] < a[min_idx]:
                min_idx = j
        if min_idx != i:
            a[i], a[min_idx] = a[min_idx], a[i]
            swaps += 1
    return comparisons, swaps

def insertion_sort(arr):
    a = arr.copy()
    n = len(a)
    comparisons = 0
    shifts = 0
    for i in range(1, n):
        key = a[i]
        j = i - 1
        while j >= 0:
            comparisons += 1
            if a[j] > key:
                a[j + 1] = a[j]
                shifts += 1
                j -= 1
            else:
                break
        a[j + 1] = key
    return comparisons, shifts

def run_experiment():
    N = 1000
    
    cases = {
        "Best Case (Đã tăng dần)": list(range(1, N + 1)),
        "Worst Case (Giảm dần)": list(range(N, 0, -1)),
        "Average Case (Ngẫu nhiên)": [random.randint(1, 10000) for _ in range(N)]
    }
    
    header_format = "| {:<25} | {:<20} | {:<16} | {:<16} | {:<16} |"
    row_format = "| {:<25} | {:<20} | {:<16,} | {:<16,} | {:<16,} |"
    divider = "-" * 105
    
    print(divider)
    print(header_format.format("Trường hợp dữ liệu", "Tiêu chí", "Insertion Sort", "Bubble Sort", "Selection Sort"))
    print(divider)
    
    for case_name, data in cases.items():
        ins_comp, ins_move = insertion_sort(data)
        bub_comp, bub_move = bubble_sort(data)
        sel_comp, sel_move = selection_sort(data)
        
        print(row_format.format(case_name, "Số phép so sánh", ins_comp, bub_comp, sel_comp))
        print(row_format.format("", "Số Swap / Shift", ins_move, bub_move, sel_move))
        print(divider)

if __name__ == "__main__":
    run_experiment()