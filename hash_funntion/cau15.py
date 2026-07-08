class MinHash:
    def __init__(self):
        self.a = [3, 5, 7]
        self.b = [1, 2, 3]
        self.p = 101

    def signature(self, s):
        sig = []
        for i in range(len(self.a)):
            mn = self.p
            for x in s:
                h = (self.a[i] * x + self.b[i]) % self.p
                if h < mn:
                    mn = h
            sig.append(mn)
        return sig

A = {1, 2, 3, 4, 5}
B = {3, 4, 5, 6, 7}
mh = MinHash()
sigA = mh.signature(A)
sigB = mh.signature(B)
same = 0
for i in range(len(sigA)):
    if sigA[i] == sigB[i]:
        same += 1
estimate = same / len(sigA)
intersection = len(A & B)
union = len(A | B)
jaccard = intersection / union
print("Signature A:", sigA)
print("Signature B:", sigB)
print("Jaccard xấp xỉ:", estimate)
print("Jaccard thật:", jaccard)