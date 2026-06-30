class Double:
    def __init__(self, capacity = 4):
        self.capacity = capacity
        self.size = 0
        self.data = [None] * capacity

    def append(self, value):
        if self.size == self.capacity:
            self.resize()
        self.data[self.size] = value
        self.size += 1

    def resize(self):
        self.capacity *= 2
        new_data = [None] * self.capacity
        for i in range(self.size):
            new_data[i] = self.data[i]
        self.data = new_data

a = Double()
a.append(1)
a.append(2)
a.append(3)
a.append(4)

print(a.capacity)

a.append(5)

print(a.capacity)