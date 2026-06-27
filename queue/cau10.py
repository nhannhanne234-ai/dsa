class SimplePriorityQueue:
    def __init__(self):
        self.queue = []

    def push(self, value):
        self.queue.append(value)
        self.queue.sort()

    def pop(self):
        return self.queue.pop(0) if self.queue else None

pq = SimplePriorityQueue()
for x in [3, 1, 4, 2]:
    pq.push(x)
print(pq.pop())