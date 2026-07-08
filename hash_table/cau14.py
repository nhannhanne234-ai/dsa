class HashTable:
    DELETED = object()
    def __init__(self, size=10):
        self.size = size
        self.table = [None] * size

    def _hash(self, key):
        return hash(key) % self.size

    def put(self, key, value):
        index = self._hash(key)
        for _ in range(self.size):
            if self.table[index] is None or self.table[index] is self.DELETED:
                self.table[index] = (key, value)
                return
            if self.table[index][0] == key:
                self.table[index] = (key, value)
                return
            index = (index + 1) % self.size

    def get(self, key):
        index = self._hash(key)
        for _ in range(self.size):
            if self.table[index] is None:
                return None
            if (self.table[index] is not self.DELETED and
                    self.table[index][0] == key):
                return self.table[index][1]
            index = (index + 1) % self.size
        return None

    def remove(self, key):
        index = self._hash(key)
        for _ in range(self.size):
            if self.table[index] is None:
                return False
            if (self.table[index] is not self.DELETED and
                    self.table[index][0] == key):
                self.table[index] = self.DELETED
                return True
            index = (index + 1) % self.size
        return False

ht = HashTable(5)
ht.put("A", 10)
ht.put("B", 20)
print(ht.get("B"))
ht.remove("B")
print(ht.get("B"))