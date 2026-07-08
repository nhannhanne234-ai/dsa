def hash_modulo(k, m):
    return k % m

m = 10
keys = [37, 15, 28, 44, 59, 72, 81]
for k in keys:
    print(f"k={k} -> {hash_modulo(k, m)}")