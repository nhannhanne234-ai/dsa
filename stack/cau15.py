class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        return None

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        return None

    def is_empty(self):
        return len(self.items) == 0

def sort_stack(src_stack):
    tmp_stack = Stack()
    while not src_stack.is_empty():
        tmp = src_stack.pop()
        while not tmp_stack.is_empty() and tmp_stack.peek() > tmp:
            src_stack.push(tmp_stack.pop())
        tmp_stack.push(tmp)
    return tmp_stack.items

s = Stack()
for x in [3, 1, 2]:
    s.push(x)
print(sort_stack(s))