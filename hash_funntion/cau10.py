def multiplication_hash(k, m):
    A = 0.618
    return int(m * ((k * A) % 1))

def division_hash(k, m):
    return k % m

keys = [10, 20, 30, 40, 50]
m = 10

print("nhân:")
for k in keys:
    print(k, "->", multiplication_hash(k, m))

print("chia:")
for k in keys:
    print(k, "->", division_hash(k, m))