# Bubble Sort
def bubble_sort(arr):                                   # định nghĩa hàm 
    for i in range(len(arr)):                           # vòng lặp duyệt qua số lượng của mảng
        for j in range(len(arr) - 1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]     # hoán đổi hai phần tử

arr = [120, 35, 60, 42, 280, 7, 15, 19]
bubble_sort(arr)
print(arr)

# Nhận xét:
# - Input: mảng các số nguyên chưa sắp xếp
# - Output: chính mảng đó đã được sắp xếp lại theo thứ tự tăng dần
# - Sắp xếp trực tiếp từ mảng ban đầu, không tốn bộ nhớ