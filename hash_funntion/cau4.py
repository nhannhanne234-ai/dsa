def hash_modulo(k, m):
    return k % m
keys = [15, 25, 35, 12, 22, 44, 54]
m = 10

buckets = {}
collisions = 0
for key in keys:
    bucket = hash_modulo(key, m)
    if bucket in buckets:
        collisions += 1
    else:
        buckets[bucket] = []
    buckets[bucket].append(key)
print("số va chạm:", collisions)