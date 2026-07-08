class HashTable:
    def __init__(self, size=10):
        self.size = size
        self.table = [None] * size
        self.DELETED = ("<deleted>", None)

    def _hash(self, key):
        return hash(key) % self.size

    def put(self, key, value):
        index = self._hash(key)
        for _ in range(self.size):
            if self.table[index] is None or self.table[index] == self.DELETED:
                self.table[index] = (key, value)
                return
            if self.table[index][0] == key:
                self.table[index] = (key, value)
                return
            index = (index + 1) % self.size
        print("hash table đầy")

    def get(self, key):
        index = self._hash(key)
        for _ in range(self.size):
            if self.table[index] is None:
                return None
            if self.table[index] != self.DELETED and self.table[index][0] == key:
                return self.table[index][1]
            index = (index + 1) % self.size
        return None

    def remove(self, key):
        index = self._hash(key)
        for _ in range(self.size):
            if self.table[index] is None:
                return False
            if self.table[index] != self.DELETED and self.table[index][0] == key:
                self.table[index] = self.DELETED
                return True
            index = (index + 1) % self.size
        return False

    def display(self):
        for i, item in enumerate(self.table):
            print(f"{i}: {item}")

ht = HashTable(5)
ht.put("a", 1)
ht.put("b", 2)
ht.put("c", 3)
print("get('a') =", ht.get("a"))
ht.remove("b")
ht.display()