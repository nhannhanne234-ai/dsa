# Bubble Sort
def bubbleSort(arr):
    for i in range(len(arr)):
        for j in range(0, len(arr) - i - 1):
            if arr[j] > arr[j + 1]:
                temp = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = temp
                
arr = [25, 17, 7, 14, 6, 3, 100, -2,-10,-50]
print("mảng chưa được sắp xếp là: ", arr )
bubbleSort(arr)

print('mảng được sắp xếp là: ', arr)

# Nhận xét
# - Input: một mảng xáo trộn gồm 10 số nguyên bao gồm ăm và dương
# - Output: mảng ban đầu đã được sắp xếp hoàn chỉnh theo thứ tự tăng dần.
# - Lợi ích tốt nhất: thuật toán rất trực quan, dễ hiểu, dễ cài đặt và không tốn thêm bộ nhớ để chạy vì sắp xếp trực tiếp trên mảng gốc