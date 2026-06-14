# Bubble Sort
def bubble_Sort(arr):
    n = len(arr)
    swapped = False
    for i in range(n-1):
        for j in range(0, n-i-1):
            if arr[j] > arr[j + 1]:
                swapped = True
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
        if not swapped:
            return
arr = [60, 32, 15, 12, 52, 71, 90, -1, -10, -30, -155, 75]
bubble_Sort(arr)
print("mảng được sắp xếp là:")
for i in range(len(arr)):
    print("% d" % arr[i], end=" ")

# Nhận xét:
# - Input: mảng các số nguyên bao gồm số âm và dương chưa được sắp xếp
# - Output: chính mảng đó đã được sắp xếp lại theo thứ tự tăng dần từ âm đến dương