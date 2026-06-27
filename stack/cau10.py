class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)
        return None

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)


class StackUseQueue:
    def __init__(self):
        self.q1 = Queue()
        self.q2 = Queue()

    def push(self, item):
        self.q1.enqueue(item)

    def pop(self):
        if self.q1.is_empty():
            return "underflow"

        while self.q1.size() > 1:
            self.q2.enqueue(self.q1.dequeue())
        pop_item = self.q1.dequeue()
        self.q1, self.q2 = self.q2, self.q1

        return pop_item

    def display(self):
        return self.q1.items

stack = StackUseQueue()

stack.push(10)
stack.push(20)
stack.push(30)
print(f"stack hiện tại: {stack.display()}")

print(f"pop: {stack.pop()}")
print(f"stack hiện tại: {stack.display()}")