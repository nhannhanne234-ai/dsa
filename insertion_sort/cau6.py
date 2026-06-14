def count_compare(a):
    n = len(a)
    compare = 0
    for i in range(1,n):
        key = a[i]
        j=i-1
        while j>=0:
            compare += 1
            if key<a[j]:
                a[j+1] = a[j]
                j-=1
            else:
                break
        a[j+1] = key
    return compare

a = [1, 2, 3]
result = count_compare(a)
print(f"{result} lần so sánh")