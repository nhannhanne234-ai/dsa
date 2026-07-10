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


def largest_rectangle_area(h):
    stack = Stack()
    max_area = 0
    heights = h + [0]
    for i in range(len(heights)):
        while not stack.is_empty() and heights[i] < heights[stack.peek()]:
            height = heights[stack.pop()]
            width = i if stack.is_empty() else i - stack.peek() - 1
            max_area = max(max_area, height * width)
        stack.push(i)
    return max_area


h = [2, 1, 5, 6, 2, 3]
ket_qua = largest_rectangle_area(h)
print(f"{ket_qua}")