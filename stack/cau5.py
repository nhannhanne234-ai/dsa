class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()

    def is_empty(self):
        return len(self.items) == 0

    def display(self):
        return self.items

    def traverse_and_count(self):
        temp_stack = Stack()
        count = 0
        elements = []

        while not self.is_empty():
            val = self.pop()
            elements.append(str(val))
            count += 1
            temp_stack.push(val)
        print(f"theo thứ tự của LIFO: {', '.join(elements)}")

        while not temp_stack.is_empty():
            self.push(temp_stack.pop())

def stack_count():
    stack = Stack()
    
    stack.push(1)
    stack.push(2)
    stack.push(3)
    
    print(f"lúc đầu: {stack.display()}")

    stack.traverse_and_count()
    
    print(f"trạng thái kiểm tra lại (là như lúc đầu): {stack.display()}")

stack_count()