def hash_string(s, m):
    total = 0
    for ch in s:
        total += ord(ch)
    return total % m

m = 10
s1 = "abc"
s2 = "cba"
print(f"{s1} -> {hash_string(s1, m)}")
print(f"{s2} -> {hash_string(s2, m)}")