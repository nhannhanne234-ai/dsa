class AmortizedQueue:
    def __init__(self):
        self.in_stack = []
        self.out_stack = []

    def enqueue(self, value):
        self.in_stack.append(value)

    def dequeue(self):
        if not self.out_stack:
            while self.in_stack:
                self.out_stack.append(self.in_stack.pop())
        if not self.out_stack:
            return None
        return self.out_stack.pop()

aq = AmortizedQueue()
aq.enqueue(1)
aq.enqueue(2)
aq.enqueue(3)
print(aq.dequeue())
print(aq.dequeue())