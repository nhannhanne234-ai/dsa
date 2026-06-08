class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

# hàm thêm một phần tử vào cuối danh sách để tiện tạo test case
    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

# hàm in danh sách liên kết theo định dạng yêu cầu
    def print_list(self):
        current = self.head
        elements = []
        while current:
            elements.append(str(current.data))
            current = current.next
        elements.append("null")
        print("-".join(elements))

# cài đặt Bubble Sort hoán đổi giá trị
    def bubble_sort(self):
        if not self.head or not self.head.next:
            return

        was_swapped = True
        while was_swapped:
            was_swapped = False
            current = self.head
            
            # Duyệt qua các cặp liền kề cho đến nút cuối cùng
            while current and current.next:
                if current.data > current.next.data:
                    # Hoán đổi giá trị (data) của hai nút liền kề 
                    current.data, current.next.data = current.next.data, current.data
                    was_swapped = True
                current = current.next

# --- Chạy thử nghiệm với Ví dụ từ đề bài ---
if __name__ == "__main__":
    ll = LinkedList()
    # Khởi tạo danh sách: 1-3-2-null [cite: 65]
    ll.append(1)
    ll.append(3)
    ll.append(2)

    print("Danh sách ban đầu:")
    ll.print_list()

    # Thực hiện sắp xếp
    ll.bubble_sort()

    print("Danh sách sau khi sắp xếp:")
    ll.print_list()

# bài này có dùng AI