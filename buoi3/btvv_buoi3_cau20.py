# hàm trộn hai nửa đã sắp xếp và đếm số cặp nghịch thế xuất hiện giữa hai nửa
def merge_and_count(a, temp_arr, left, mid, right):
    i = left                                                                    # con trỏ duyệt nửa bên trái (từ left đến mid)
    j = mid + 1                                                                 # con trỏ duyệt nửa bên phải (từ mid+1 đến right)
    k = left                                                                    # con trỏ để điền phần tử vào mảng tạm temp_arr
    inv_count = 0                                                               # biến đếm số cặp nghịch thế (số swap)

# duyệt qua cả hai nửa mảng
    while i <= mid and j <= right:
        if a[i] <= a[j]:                                                        # thằng bên trái nhỏ hơn hoặc bằng -> Đứng đúng thứ tự tăng dần
            temp_arr[k] = a[i]
            i += 1
        else:                                                                   # thằng bên phải nhỏ hơn thằng bên trái -> Vi phạm! Xuất hiện nghịch thế!
            temp_arr[k] = a[j]

# điểm chính: Vì nửa trái đã xếp tăng dần, nếu a[i] > a[j] 
# thì TẤT CẢ các phần tử từ a[i] đến a[mid] đều sẽ lớn hơn a[j].
# số lượng cặp nghịch thế tạo ra chính là số phần tử còn lại của nửa trái.
            inv_count += (mid - i + 1)
            j += 1
        k += 1

    while i <= mid:                                                             # nếu nửa bên trái còn phần tử sót lại, bốc hết vào mảng tạm
        temp_arr[k] = a[i]
        i += 1
        k += 1

    while j <= right:                                                           # nếu nửa bên phải còn phần tử sót lại, bốc hết vào mảng tạm
        temp_arr[k] = a[j]
        j += 1
        k += 1

    for loop_index in range(left, right + 1):                                   # sao chép các phần tử đã sắp xếp từ mảng tạm temp_arr trả lại mảng gốc a
        a[loop_index] = temp_arr[loop_index]
        
    return inv_count

# hàm đệ quy chia đôi mảng và cộng dồn số cặp nghịch thế
def merge_sort_and_count(a, temp_arr, left, right):
    inv_count = 0
    if left < right:
        mid = (left + right) // 2                                               # tìm vị trí chính giữa để chia đôi

        inv_count += merge_sort_and_count(a, temp_arr, left, mid)               # 1. đếm số nghịch thế ở nửa bên trái

        inv_count += merge_sort_and_count(a, temp_arr, mid + 1, right)          # 2. đếm số nghịch thế ở nửa bên phải

        inv_count += merge_and_count(a, temp_arr, left, mid, right)             # 3. đếm số nghịch thế khi TRỘN hai nửa lại với nhau

    return inv_count

# hàm chính để gọi từ bên ngoài.
def count_swaps_fast(a):
    n = len(a)
    temp_arr = [0] * n                                                          # tạo một mảng tạm để phục vụ việc trộn
    return merge_sort_and_count(a, temp_arr, 0, n - 1)                          # gọi hàm đệ quy chạy từ chỉ số 0 đến n-1


a = [2, 3, 1]
mang_goc = a.copy()                                                             # tạo một bản sao để mảng gốc không bị thay đổi khi in thông báo
total_swaps = count_swaps_fast(a)

print(f"Mảng ban đầu: {mang_goc}")
print(f"Số swap nếu dùng Bubble Sort là: {total_swaps} lần.")


# bài này có dùng AI hỗ trợ để viết code:(((