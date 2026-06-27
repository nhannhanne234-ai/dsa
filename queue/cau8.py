class Deque:
    def __init__(self):
        self.items = []

    def pushFront(self, value):
        self.items.insert(0, value)

    def pushBack(self, value):
        self.items.append(value)

    def popFront(self):
        return self.items.pop(0) if self.items else None

    def popBack(self):
        return self.items.pop() if self.items else None

dq = Deque()
dq.pushFront(1)
dq.pushBack(2)
print(dq.items)