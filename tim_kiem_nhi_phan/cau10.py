def rotated_sorted_array(a, x):
    left = 0
    right = len(a) - 1
    
    while left <= right:
        mid = (left + right) // 2
        
        if a[mid] == x:                     # nếu thấy mid bằng x
            return mid                      # trả về luôn kết quả
        
        if a[left] <= a[mid]:
            if a[left] <= x < a[mid]:       # kiểm tra x có nằm trong vùng bên trái không
                right = mid - 1
            else:
                left = mid + 1
        else:
            if a[mid] < x <= a[right]:
                left = mid + 1
            else:
                right = mid - 1
    return -1

a = [4, 5, 6, 7, 0, 1, 2]
x = int(input("Nhập: "))

result = rotated_sorted_array(a, x)

print(f"Chỉ số của x = {x} trong mảng là: {result}")