def hash1(k, m):
    return k % m

def hash2(k, m):
    return (k * 7 + 3) % m

keys = list(range(100))
m = 10
buckets1 = [0] * m
buckets2 = [0] * m

for k in keys:
    buckets1[hash1(k, m)] += 1
    buckets2[hash2(k, m)] += 1

expected = len(keys) / m
chi1 = 0
chi2 = 0

for count in buckets1:
    chi1 += (count - expected) ** 2 / expected

for count in buckets2:
    chi2 += (count - expected) ** 2 / expected

print("Hash 1:", buckets1)
print("Chi-square:", chi1)
print("Hash 2:", buckets2)
print("Chi-square:", chi2)