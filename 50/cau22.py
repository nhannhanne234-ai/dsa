class MinStack:
    def __init__(self):
        self.items = []
        self.min_stack = []

    def push(self, item):
        self.items.append(item)
        if len(self.min_stack) == 0 or item <= self.min_stack[-1]:
            self.min_stack.append(item)

    def pop(self):
        if self.is_empty():
            return None
        pop_item = self.items.pop()
        if pop_item == self.min_stack[-1]:
            self.min_stack.pop()
        return pop_item

    def getMin(self):
        if len(self.min_stack) == 0:
            return None
        return self.min_stack[-1]

    def is_empty(self):
        return len(self.items) == 0

stack = MinStack()

stack.push(5)
print(f"push 5 -> getMin = {stack.getMin()}")

stack.push(3)
print(f"push 3 -> getMin = {stack.getMin()}")

stack.push(7)
print(f"push 7 -> getMin = {stack.getMin()}")