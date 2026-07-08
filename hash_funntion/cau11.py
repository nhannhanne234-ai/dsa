def set_hash(arr):
    h = 0
    for x in arr:
        h ^= x
    return h

s1 = [1, 2, 3]
s2 = [3, 1, 2]

print(set_hash(s1))
print(set_hash(s2))