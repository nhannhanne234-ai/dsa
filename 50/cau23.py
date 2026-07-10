class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        return None

    def is_empty(self):
        return len(self.items) == 0


def evaluate_rpn(expression):
    stack = Stack()
    token = expression.split()

    for i in token:
        if i in ("+", "-", "*", "/"):
            b = stack.pop()
            a = stack.pop()

            if i == "+":
                result = a + b
            elif i == "-":
                result = a - b
            elif i == "*":
                result = a * b
            elif i == "/":
                result = int(a / b)
            stack.push(result)
        else:
            stack.push(int(i))
            
    return stack.pop()

bieu_thuc = "3 4 + 2 *"
ket_qua = evaluate_rpn(bieu_thuc)

print(f"'{bieu_thuc}' -> {ket_qua}")