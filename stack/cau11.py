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

def next_greater_element(a):
    stack = Stack()
    result = [-1] * len(a)
    for i in range(len(a)):
        while not stack.is_empty() and a[i] > a[stack.peek()]:
            prev_index = stack.pop()
            result[prev_index] = a[i]
        stack.push(i)
        
    return result

a = [2, 1, 3]
output = next_greater_element(a)

print(f"{output}")