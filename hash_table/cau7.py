class HashTable:
    def __init__(self, size=4):
        self.size = size
        self.count = 0
        self.table = [[] for _ in range(size)]

    def _hash(self, key):
        return hash(key) % self.size

    def load_factor(self):
        return self.count / self.size

    def put(self, key, value):
        if self.load_factor() > 0.75:
            self.rehash()
        index = self._hash(key)
        for pair in self.table[index]:
            if pair[0] == key:
                pair[1] = value
                return
        self.table[index].append([key, value])
        self.count += 1

    def get(self, key):
        index = self._hash(key)
        for k, v in self.table[index]:
            if k == key:
                return v
        return None

    def rehash(self):
        old_table = self.table
        self.size *= 2
        self.table = [[] for _ in range(self.size)]
        self.count = 0
        for bucket in old_table:
            for key, value in bucket:
                self.put(key, value)

    def display(self):
        for i, bucket in enumerate(self.table):
            print(f"{i}: {bucket}")

ht = HashTable(4)
ht.put("A", 10)
ht.put("B", 20)
ht.put("C", 30)
ht.put("D", 40)
print(ht.load_factor())
ht.put("E", 50)
ht.display()