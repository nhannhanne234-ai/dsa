class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

class HashTable:
    def __init__(self, size=10):
        self.size = size
        self.table = [None] * size

    def _hash(self, key):
        return hash(key) % self.size

    def put(self, key, value):
        index = self._hash(key)
        head = self.table[index]
        current = head
        while current:
            if current.key == key:
                current.value = value
                return
            current = current.next
        new_node = Node(key, value)
        new_node.next = head
        self.table[index] = new_node

    def get(self, key):
        index = self._hash(key)
        current = self.table[index]
        while current:
            if current.key == key:
                return current.value
            current = current.next
        return None

    def remove(self, key):
        index = self._hash(key)
        current = self.table[index]
        prev = None
        while current:
            if current.key == key:
                if prev:
                    prev.next = current.next
                else:
                    self.table[index] = current.next
                return True
            prev = current
            current = current.next
        return False

    def display(self):
        for i in range(self.size):
            print(f"Bucket {i}:", end=" ")
            current = self.table[i]
            while current:
                print(f"({current.key}:{current.value})", end=" -> ")
                current = current.next
            print("None")

ht = HashTable()
ht.put('a', 1)
ht.put('b', 2)
ht.put('c', 3)
print("get('a') =", ht.get('a'))
ht.remove('b')
print("\nHash Table:")
ht.display()