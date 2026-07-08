class HashSet:
    def __init__(self, size=10):
        self.size = size
        self.table = [[] for _ in range(size)]

    def _hash(self, value):
        return hash(value) % self.size

    def add(self, value):
        index = self._hash(value)
        if value not in self.table[index]:
            self.table[index].append(value)

    def contains(self, value):
        index = self._hash(value)
        return value in self.table[index]

    def remove(self, value):
        index = self._hash(value)
        if value in self.table[index]:
            self.table[index].remove(value)

    def display(self):
        result = []
        for bucket in self.table:
            result.extend(bucket)
        print(set(result))

s = HashSet()
s.add(1)
s.add(1)
s.add(2)
print(s.contains(1))
print(s.contains(3))
s.remove(1)
print(s.contains(1))
s.display()