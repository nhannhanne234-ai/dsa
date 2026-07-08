# chaining
class ChainingHashTable:
    def __init__(self, size=5):
        self.size = size
        self.table = [[] for _ in range(size)]

    def put(self, key, value):
        index = hash(key) % self.size
        for pair in self.table[index]:
            if pair[0] == key:
                pair[1] = value
                return
        self.table[index].append([key, value])

    def get(self, key):
        index = hash(key) % self.size
        for k, v in self.table[index]:
            if k == key:
                return v
        return None

    def remove(self, key):
        index = hash(key) % self.size
        for i, (k, v) in enumerate(self.table[index]):
            if k == key:
                self.table[index].pop(i)
                return True
        return False
    
# chaining
ht = ChainingHashTable(5)
ht.put("A", 10)
ht.put("B", 20)
ht.put("C", 30)
print("Get A:", ht.get("A"))
ht.remove("B")
print("Get B:", ht.get("B"))



# open addressing
class OpenAddressHashTable:
    def __init__(self, size=5):
        self.size = size
        self.table = [None] * size
        self.DELETED = ("DEL", None)

    def put(self, key, value):
        index = hash(key) % self.size
        while self.table[index] not in (None, self.DELETED):
            if self.table[index][0] == key:
                self.table[index] = (key, value)
                return
            index = (index + 1) % self.size
        self.table[index] = (key, value)

    def get(self, key):
        index = hash(key) % self.size
        for _ in range(self.size):
            if self.table[index] is None:
                return None
            if self.table[index] != self.DELETED and self.table[index][0] == key:
                return self.table[index][1]
            index = (index + 1) % self.size
        return None

    def remove(self, key):
        index = hash(key) % self.size
        for _ in range(self.size):
            if self.table[index] is None:
                return False
            if self.table[index] != self.DELETED and self.table[index][0] == key:
                self.table[index] = self.DELETED
                return True
            index = (index + 1) % self.size
        return False

# opne addressing
ht = OpenAddressHashTable(5)
ht.put("A", 10)
ht.put("B", 20)
ht.put("C", 30)
print("Get A:", ht.get("A"))
ht.remove("B")
print("Get B:", ht.get("B"))