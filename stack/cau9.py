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


def infix_to_postfix(expression):
    order_of_priority = {'+': 1, '-': 1, '*': 2, '/': 2}
    stack = Stack()
    output = []
    
    for char in expression:
        if char == ' ':
            continue
            
        if char.isalnum():
            output.append(char)
            
        elif char == '(':
            stack.push(char)
            
        elif char == ')':
            while not stack.is_empty() and stack.peek() != '(':
                output.append(stack.pop())
            stack.pop()
            
        elif char in order_of_priority:
            while (not stack.is_empty() and stack.peek() in order_of_priority and 
                   order_of_priority[stack.peek()] >= order_of_priority[char]):
                output.append(stack.pop())
            stack.push(char)
            
    while not stack.is_empty():
        output.append(stack.pop())
        
    return ' '.join(output)


co_san = "a+b*c"
ket_qua = infix_to_postfix(co_san)

print(f"'{co_san}' -> '{ket_qua}'")