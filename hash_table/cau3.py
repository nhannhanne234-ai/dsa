class HashTable:
    def __init__(self, size=10):
        self.size = size
        self.table = [[] for _ in range(size)]

    def _hash(self, key):
        return hash(key) % self.size

    def put(self, key, value):
        index = self._hash(key)
        for pair in self.table[index]:
            if pair[0] == key:
                pair[1] = value
                return
        self.table[index].append([key, value])

    def get(self, key):
        index = self._hash(key)
        for k, v in self.table[index]:
            if k == key:
                return v
        return None


a = ['a', 'b', 'a', 'c', 'a']

ht = HashTable()

for x in a:
    count = ht.get(x)
    if count is None:
        ht.put(x, 1)
    else:
        ht.put(x, count + 1)

for bucket in ht.table:
    for key, value in bucket:
        print(f"{key}: {value}")