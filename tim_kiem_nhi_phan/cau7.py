def lower_bound(a, x):
    n = len(a)
    left = 0
    right = n - 1
    ans = n                             # trả về n nếu không tìm thấy phần tử nào >= x

    while left <= right:
        mid = (left + right) // 2
        
        if a[mid] > x:
            ans = mid                   # ghi lại vị trí mà >= x
            right = mid - 1             # đẩy sang trái để tìm phần tử nhỏ hơn
        else:
            left = mid + 1              # phần tử nhỏ hơn x thì đẩy sang phải để tìm

    return ans

a = [1, 3, 5, 7]
x = int(input("Nhập: "))
print(f"Chỉ số của lower bound của {x} là: {lower_bound(a, x)}")