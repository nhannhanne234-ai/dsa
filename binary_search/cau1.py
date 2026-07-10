def location_of_index(a, x):
    left = 0
    right = len(a) - 1

    while left <= right:
        mid = (left + right) // 2
        if a[mid] == x:             # nếu thấy mid == số đang tìm
            return mid              # trả về kết quả mid == x
        elif a[mid] < x:
            left = mid + 1          # vì x lớn hơn mid nên x sẽ nằm bên phải mid, bỏ hết bên trái, trái trở thành mid + 1 vì khi đó x != mid
        else:
            right = mid - 1         # ngược lại với left ở trên

    return -1                       # trả về -1 nếu không thấy x trong mảng

a = [1, 3, 5, 7, 9]
x = int(input("Nhập số cần tìm index: "))
result = location_of_index(a, x)
print(f"Số {x} được tìm thấy tại vị trí {result} trong mảng")