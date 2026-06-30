class ArrayList:
    def __init__(self, capacity=1):
        self.capacity = capacity
        self.size = 0
        self.data = [None] * capacity
        self.copy_count = 0

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
            self.copy_count += 1
        self.data = new_data


n = 36
a = ArrayList()

for i in range(n):
    a.append(i)

print(a.copy_count)