def heap_push(heap, item):
    """Thêm một phần tử vào Min-Heap và tự động sắp xếp lại cây."""
    heap.append(item)          # Bước 1: Thêm phần tử mới vào cuối mảng
    i = len(heap) - 1          # Vị trí (chỉ số) của phần tử vừa thêm
    
    # Bước 2: Vun đống ngược lên (Up-heap / Sift-up)
    while i > 0:
        parent = (i - 1) // 2  # Tìm chỉ số của nút cha
        
        # Nếu nút hiện tại đã lớn hơn hoặc bằng nút cha, cấu trúc Min-Heap đã hợp lệ
        if heap[i] >= heap[parent]:
            break
            
        # Nếu nút hiện tại nhỏ hơn nút cha, tiến hành đổi chỗ
        heap[i], heap[parent] = heap[parent], heap[i]
        
        # Di chuyển chỉ số lên nút cha để tiếp tục kiểm tra vòng lặp
        i = parent

    return heap

heap = [10, 20, 30]
item = 15

print(heap_push(heap, item))