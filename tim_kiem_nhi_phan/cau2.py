def index_find(a, x):
    left = 0
    right = len(a) - 1

    while left <= right:
        mid = (left + right) // 2
        if a[mid] == x:             # nếu thấy mid == số đang tìm
            return True
        elif a[mid] < x:
            left = mid + 1          # vì x lớn hơn mid nên x sẽ nằm bên phải mid, bỏ hết bên trái, trái trở thành mid + 1 vì khi đó x != mid
        else:
            right = mid - 1         # ngược lại với left ở trên

    return False                    # trả về -1 nếu không thấy x trong mảng

a = [2, 4, 6, 8]
x = int(input("Nhập số cần tìm: "))
result = index_find(a, x)
print(f"Số {x} được tìm thấy trong mảng")