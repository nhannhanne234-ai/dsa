class QuadraticHashTable:
    def __init__(self, size=11):
        self.size = size
        self.table = [None] * size

    def h1(self, key):
        return hash(key) % self.size

    def put(self, key, value):
        index = self.h1(key)
        for i in range(self.size):
            new_index = (index + i * i) % self.size
            if self.table[new_index] is None:
                self.table[new_index] = (key, value)
                return
            if self.table[new_index][0] == key:
                self.table[new_index] = (key, value)
                return

    def get(self, key):
        index = self.h1(key)
        for i in range(self.size):
            new_index = (index + i * i) % self.size
            if self.table[new_index] is None:
                return None
            if self.table[new_index][0] == key:
                return self.table[new_index][1]
        return None
    
ht = QuadraticHashTable()
ht.put("A", 10)
ht.put("B", 20)
ht.put("C", 30)
print(ht.get("B"))