def bubble_sort_benchmark(a):
    n = len(a)
    compare_count = 0                                                   # biến đếm số lần so sánh (mỗi khi chạy lệnh if)
    swap_count = 0                                                      # biến đếm số lần đổi chỗ (swap)
    
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            compare_count += 1                                          # cứ vào so sánh là tăng bộ đếm lên 1
            
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]                         # hoán đổi
                swap_count += 1                                         # thực hiện swap thành công thì tăng lên 1
                swapped = True
                
        if not swapped:
            break
            
    return compare_count, swap_count

a = [25, 14, 36, 5, 8, 19, 1, 40]
compare, swap = bubble_sort_benchmark(a)

print(f"Số lần so sánh: {compare} lần")
print(f"Số lần hoán đổi: {swap} lần")
print(f"Mảng sau khi xếp: {a}")