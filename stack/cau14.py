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

def stock_span(prices):
    stack = Stack()
    span = []
    for i in range(len(prices)):
        while not stack.is_empty() and prices[stack.peek()] <= prices[i]:
            stack.pop()
        days = i + 1 if stack.is_empty() else i - stack.peek()
        span.append(days)
        stack.push(i)
    return span

prices = [100, 80, 60, 70, 60, 75, 85]
print(stock_span(prices))