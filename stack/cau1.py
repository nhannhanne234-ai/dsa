class Stack:
    def __init__(self, max_size):
        self.max_size = max_size
        self.arr = [None] * max_size                    # tạo mảng với kích thước max_size
        self.top_index = -1                             # lúc đầu là ngăn xếp rỗng

    def is_empty(self):
        return self.top_index == -1                     # xem coi có rỗng không
    
    # def is_empty(self):
    #     if self.top_index == -1:
    #         return True
    #     else:
    #         return False

    def is_full(self):
        return self.top_index == self.max_size - 1      # xem coi có đầy không
    
    # def is_full(self):
    #     if self.top_index == self.max_size - 1:
    #         return True
    #     else:
    #         return False
    
    def push(self, value):                              # này là nhét vào
        if self.is_full():                              # nếu đầy
            print(f"ngăn xếp đầy")
            return None
        
        # không thì:
        self.top_index += 1                             # biến này tăng 1
        self.arr[self.top_index] = value                # chỗ này gán giá trị sao khi index tăng trong mảng thành value
        # print(f"đã push: {value}")

    def pop(self):                                      # này là bứng ra
        if self.is_empty():                             # nếu rỗng
            print(f"ngăn xếp rỗng")
            return None
        
        temp = self.arr[self.top_index]                 # cho temp = cái index mới nhất(theo cách hiểu)
        self.arr[self.top_index] = None                 # tại index đó thì gán lại None vì đã bóc ra
        self.top_index -= 1                             # biến này giảm 1
        return temp                                     # đưa ra cái biến vừa bóc, cái mà cho tại index
    
    def top(self):
        if self.is_empty():                             # nếu rỗng
            print(f"ngăn xếp rỗng")
            return None
        return self.arr[self.top_index]                 # trả về cái mới nhất vừa được nhét vào
    
    # def print_stack(self):
    #     if self.is_empty():
    #         print("Ngăn xếp rỗng, không có gì để in.")
    #         return

    #     for i in range(self.top_index, -1, -1):
    #         print(self.arr[i], end=" ")

if __name__ == "__main__":
    s = Stack(10)
    s.push(1)
    s.push(2)
    s.push(3)

    popped_value = s.pop()
    print(f"pop: {popped_value}")
    # print(s.print_stack())