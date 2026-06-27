class CircularQueue:
    def __init__(self, n):
        self.n = n
        self.queue = [None] * n
        self.front = 0
        self.rear = -1
        self.size = 0

    def enqueue(self, value):
        if self.size == self.n:
            return False
        self.rear = (self.rear + 1) % self.n
        self.queue[self.rear] = value
        self.size += 1
        return True

    def dequeue(self):
        if self.size == 0:
            return None
        value = self.queue[self.front]
        self.queue[self.front] = None
        self.front = (self.front + 1) % self.n
        self.size -= 1
        return value

cq = CircularQueue(4)
cq.enqueue(10)
cq.enqueue(20)
cq.enqueue(30)
cq.dequeue()
cq.enqueue(40)
cq.enqueue(50)
print(cq.queue)