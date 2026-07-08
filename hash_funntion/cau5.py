def hash_modulo(k, m):
    return k % m

keys = [0, 16, 32, 48, 64, 80, 96, 112]

print("m = 16")
for k in keys:
    print(k, "->", hash_modulo(k, 16))

print("m = 17")
for k in keys:
    print(k, "->", hash_modulo(k, 17))