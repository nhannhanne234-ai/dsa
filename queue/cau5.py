class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, value):
        self.queue.append(value)

    def get_front_rear(self):
        if not self.queue:
            return None, None
        return self.queue[0], self.queue[-1]

q = Queue()
for x in [4, 5, 6]: q.enqueue(x)
front, rear = q.get_front_rear()
print(f"front={front}, rear={rear}")