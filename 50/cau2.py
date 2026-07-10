# đầu
def first_index(a, x):
    left = 0
    right = len(a) - 1
    ans = -1

    while left <= right:
        mid = (left + right) // 2
        if a[mid] == x:             # nếu thấy mid == số đang tìm
            ans = mid               # tạm gán vào ans khi tìm thấy để xét về dần về đầu mảng
            right = mid - 1         # đẩy dần về đầu mảng
        elif a[mid] < x:
            left = mid + 1
        else:
            right = mid - 1         # ngược lại với left ở trên

    return ans                      # trả về -1 nếu không thấy x trong mảng

a = [1, 3, 3, 5, 5, 5, 7, 7, 9]
x = int(input("Nhập số cần tìm : "))
result = first_index(a, x)
print(f"Số {x} được tìm thấy vị trí đầu tiên tại index {result} trong mảng")



# cuối
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



# đếm
def first_index(a, x):
    left = 0
    right = len(a) - 1
    ans = -1                        # để lưu kết quả tạm thời nếu thấy kết quả, ngược lại trả về -1

    while left <= right:
        mid = (left + right) // 2
        if a[mid] == x:             # nếu thấy mid == số đang tìm
            ans = mid               # tạm gán vào ans khi tìm thấy để xét về dần về đầu mảng
            right = mid - 1         # đẩy dần về đầu mảng
        elif a[mid] < x:
            left = mid + 1
        else:
            right = mid - 1         # ngược lại với left ở trên

    return ans                      # trả về -1 nếu không thấy x trong mảng

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

def count(a, x):
    first_idx = first_index(a, x)
    
    if first_idx == -1:             # nếu không tìm thấy vị trí đầu tiên thì x không tồn tại
        return 0
        
    last_idx = last_index(a, x)
    
    return last_idx - first_idx + 1

a = [1, 3, 3, 5, 5, 5, 5, 7, 7, 9]
x = int(input("Nhập số cần tìm số lần xuất hiện trong mảng: "))
print(f"Số cần đếm là {x}")
print(f"Số {x} xuất hiện {count(a, x)} lần trong mảng")