class SimulationQueue:
    def __init__(self):
        self.queue = []

    def enqueue(self, value):
        self.queue.append(value)

    def dequeue(self):
        if len(self.queue) == 0:
            return None
        return self.queue.pop(0)

def simulate(operations):
    sq = SimulationQueue()
    for op in operations:
        if op.startswith("enq"):
            val = int(op.split()[1])
            sq.enqueue(val)
        elif op == "deq":
            res = sq.dequeue()
            if res is not None:
                print(res)

operations = ["enq 5", "enq 7", "deq"]
simulate(operations)