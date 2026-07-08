def rabin_karp(text, pattern):
    n = len(text)
    m = len(pattern)
    p = 31
    mod = 1000000007
    if m > n:
        return -1
    pattern_hash = 0
    window_hash = 0
    power = 1
    for i in range(m - 1):
        power = (power * p) % mod

    for i in range(m):
        pattern_hash = (pattern_hash * p + ord(pattern[i])) % mod
        window_hash = (window_hash * p + ord(text[i])) % mod

    for i in range(n - m + 1):
        if pattern_hash == window_hash:
            if text[i:i + m] == pattern:
                return i
        if i < n - m:
            window_hash = ((window_hash - ord(text[i]) * power) * p + ord(text[i + m])) % mod
    return -1

text = "zabcd"
pattern = "abc"
print(rabin_karp(text, pattern))