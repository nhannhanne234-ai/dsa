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


def check_balanced_brackets(expression):
    stack = Stack()
    bracket_map = {")": "(", "]": "[", "}": "{"}
    
    for char in expression:
        if char in bracket_map.values():
            stack.push(char)
        elif char in bracket_map:
            if stack.is_empty():
                return False
            top_element = stack.pop()
            if bracket_map[char] != top_element:
                return False
    return stack.is_empty()


test_cases = ["([]{})", "([)]"]

for expr in test_cases:
    result = check_balanced_brackets(expr)
    print(f"'{expr}' -> {result}")