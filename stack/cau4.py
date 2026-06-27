class Stack:
    def __init__(self, max_size):
        self.items = []
        self.max_size = max_size

    def push(self, item):
        if self.is_full():
            return "overflow"
        self.items.append(item)
        return True

    def pop(self):
        if self.is_empty():
            return "underflow"
        return self.items.pop()

    def is_empty(self):
        return len(self.items) == 0

    def is_full(self):
        return len(self.items) >= self.max_size

    def display(self):
        return self.items
    
def stack_under_over():
    stack = Stack(max_size=2)
    
    test = [
        "pop",
        "push 5", 
        "push 7", 
        "push 9",
        "pop"
    ]
    
    for i in test:
        part = i.split()
        
        if part[0] == "push":
            value = int(part[1])
            result = stack.push(value)
            if result == "overflow":
                print("overflow")
                
        elif part[0] == "pop":
            value = stack.pop()
            
            if value == "underflow":
                print("underflow")
            else:
                print(f"pop: {value}")

stack_under_over()