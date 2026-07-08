def hash_tuple(a, b):
    C = 31
    return hash(a) * C ^ hash(b)

a = 10
b = 20
print(hash_tuple(a, b))