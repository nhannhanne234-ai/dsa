class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

class LRUCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = {}
        self.head = Node(0, 0)
        self.tail = Node(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head

    def remove(self, node):
        prev_node = node.prev
        next_node = node.next
        prev_node.next = next_node
        next_node.prev = prev_node

    def insertFront(self, node):
        node.next = self.head.next
        node.prev = self.head
        self.head.next.prev = node
        self.head.next = node

    def get(self, key):
        if key not in self.cache:
            return -1
        node = self.cache[key]
        self.remove(node)
        self.insertFront(node)
        return node.value

    def put(self, key, value):
        if key in self.cache:
            self.remove(self.cache[key])
        node = Node(key, value)
        self.cache[key] = node
        self.insertFront(node)
        if len(self.cache) > self.capacity:
            lru = self.tail.prev
            self.remove(lru)
            del self.cache[lru.key]

    def display(self):
        current = self.head.next
        while current != self.tail:
            print(f"({current.key}:{current.value})", end=" ")
            current = current.next
        print()

cache = LRUCache(2)
cache.put(1, 10)
cache.put(2, 20)
print("Sau khi thêm 1 và 2:")
cache.display()
print("get(1) =", cache.get(1))
print("Sau get(1):")
cache.display()
cache.put(3, 30)
print("Sau put(3,30):")
cache.display()
print("get(2) =", cache.get(2))
print("get(3) =", cache.get(3))