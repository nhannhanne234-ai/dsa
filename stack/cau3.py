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
    
def stack_simulation():
    stack = Stack()

    test = [
        "push 5",
        "push 7",
        "pop"
    ]

    for i in test:
        part = i.split()
        
        if part[0] == "push":
            stack.push(int(part[1]))
        elif part[0] == "pop":
            value = stack.pop()
            if value is not None:
                print(f"pop: {value}")
            else:
                print(f"ngăn xếp rỗng")

stack_simulation()