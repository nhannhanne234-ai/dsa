def heap_pop(heap):
    """Lấy ra và xóa phần tử nhỏ nhất (gốc) khỏi Min-Heap."""
    if not heap:
        raise IndexError("Không thể pop từ một heap rỗng!")
        
    # Nếu heap chỉ có duy nhất 1 phần tử, lấy ra và trả về luôn
    if len(heap) == 1:
        return heap.pop()
        
    root = heap[0]             # Bước 1: Giữ lại giá trị gốc (nhỏ nhất) để trả về
    heap[0] = heap.pop()       # Bước 2: Đưa phần tử cuối cùng của mảng lên trám vào gốc
    
    i = 0                      # Chỉ số bắt đầu xét từ gốc
    n = len(heap)              # Số lượng phần tử hiện tại của heap
    
    # Bước 3: Vun đống xuôi xuống (Down-heap / Sift-down)
    # Vòng lặp chạy khi nút hiện tại vẫn còn ít nhất một nút con bên trái
    while 2 * i + 1 < n:
        left = 2 * i + 1       # Chỉ số con bên trái
        right = 2 * i + 2      # Chỉ số con bên phải
        smallest = left        # Tạm thời giả định con bên trái là nhỏ nhất
        
        # Nếu có con bên phải và giá trị của nó nhỏ hơn con bên trái
        if right < n and heap[right] < heap[left]:
            smallest = right   # Cập nhật nút con nhỏ nhất là nút bên phải
            
        # Nếu nút cha đã nhỏ hơn hoặc bằng nút con nhỏ nhất, heap đã đạt chuẩn
        if heap[i] <= heap[smallest]:
            break
            
        # Nếu không, đổi chỗ nút cha với nút con nhỏ nhất đó
        heap[i], heap[smallest] = heap[smallest], heap[i]
        
        # Cập nhật chỉ số xuống vị trí mới của nút vừa đổi để xét tiếp
        i = smallest
        
    return root                # Trả về phần tử nhỏ nhất ban đầu đã lưu