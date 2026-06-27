def reverse_queue(queue):
    stack = []
    while queue:
        stack.append(queue.pop(0))
    while stack:
        queue.append(stack.pop())
    return queue

print(reverse_queue([1, 2, 3]))