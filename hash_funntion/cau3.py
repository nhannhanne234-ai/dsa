def polynomial_hash(s, p, m):
    h = 0
    n = len(s)
    for i in range(n):
        h += ord(s[i]) * (p ** (n - 1 - i))
    return h % m

s = "abc"
p = 31
m = 1000000007
print(polynomial_hash(s, p, m))