class UniversalHash:
    def __init__(self, m):
        self.m = m
        self.p = 101
        self.a = 13
        self.b = 7

    def hash(self, k):
        return ((self.a * k + self.b) % self.p) % self.m


h = UniversalHash(10)
keys = [10, 20, 30, 40, 50]
for k in keys:
    print(k, "->", h.hash(k))