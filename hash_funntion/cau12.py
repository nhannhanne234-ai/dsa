def hash_modulo(k, m):
    return k % m

m = 10
keys = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
for k in keys:
    print(k, "->", hash_modulo(k, m))
table = [[] for _ in range(m)]

for k in keys:
    bucket = hash_modulo(k, m)
    table[bucket].append(k)

for i in range(m):
    print(i, ":", table[i])

def secure_hash(k):
    a = 13
    b = 7
    p = 101
    return ((a * k + b) % p) % m

for k in keys:
    print(k, "->", secure_hash(k))