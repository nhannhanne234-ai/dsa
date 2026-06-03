def last_index(a, x):
    left = 0
    right = len(a) - 1
    ans = -1

    while left <= right:
        mid = (left + right) // 2
        if a[mid] == x:             # nếu thấy mid == số đang tìm
            ans = mid               # tạm gán vào ans khi tìm thấy để xét về dần về đầu mảng
            left = mid + 1          # đẩy dần về cuối mảng
        elif a[mid] < x:
            left = mid + 1
        else:
            right = mid - 1         # ngược lại với left ở trên

    return ans                      # trả về -1 nếu không thấy x trong mảng

a = [1, 3, 3, 5, 5, 5, 7, 7, 9]
x = int(input("Nhập số cần tìm : "))
result = last_index(a, x)
print(f"Số {x} được tìm thấy vị trí cuối cùng tại index {result} trong mảng")