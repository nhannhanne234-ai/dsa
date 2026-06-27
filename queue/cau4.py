class FixedQueue:
    def __init__(self, capacity):
        self.capacity = capacity
        self.queue = []

    def enqueue(self, value):
        if len(self.queue) >= self.capacity:
            print("è è: hàng đợi đầy rồi")
            return
        self.queue.append(value)

    def dequeue(self):
        if len(self.queue) == 0:
            print("è è: hàng đợi rỗng kìa")
            return None
        return self.queue.pop(0)

    def count(self):
        return len(self.queue)

fq = FixedQueue(2)
fq.dequeue()
fq.enqueue(10)
fq.enqueue(20)
fq.enqueue(30)
print(fq.count())