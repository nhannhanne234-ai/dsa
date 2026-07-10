class BloomFilter:
    def __init__(self, size):
        self.size = size
        self.bits = [0] * size

    def hash1(self, x):
        return x % self.size

    def hash2(self, x):
        return (x * 7 + 3) % self.size

    def hash3(self, x):
        return (x * 11 + 5) % self.size

    def add(self, x):
        self.bits[self.hash1(x)] = 1
        self.bits[self.hash2(x)] = 1
        self.bits[self.hash3(x)] = 1

    def contains(self, x):
        return (
            self.bits[self.hash1(x)] == 1
            and self.bits[self.hash2(x)] == 1
            and self.bits[self.hash3(x)] == 1
        )

bf = BloomFilter(20)
bf.add(10)
bf.add(25)
bf.add(37)
print("10:", bf.contains(10))
print("25:", bf.contains(25))
print("50:", bf.contains(50))
found = False
for x in range(100):
    if x not in [10, 25, 37] and bf.contains(x):
        print(x)
        found = True
        break
if not found:
    print("em đâu")